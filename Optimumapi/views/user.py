from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ------------------------
"""
NOTE Need to do more reasearch on how this class is exactly working, I needed to figure out a way 
to allow any non-auth user to use the "list" method but for security i couldn't allow non-auth users 
to view the usernames and passwords of the providers so i had ChatGPT help me come up with a solution. 

NOTE My understanding of this class so far:
"*args" lets the class take any number of arguments 
When invoked the class takes an argument in this case (IsAuthenticated) and checks to see if the user is
IF the user has that permission display the values of the username and password field 
ELSE return None = "Null"

"""
class RestrictedField(serializers.Field):
    def __init__(self, permission_class, *args):
        self.permission_class = permission_class
        super().__init__(*args)

    def to_representation(self, value):
        request = self.context['request']
        view = self.context.get('view', None)
        if self.permission_class().has_permission(request, view):
            return value
        return None

# ------------------------

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Users

    Arguments:
        serializers
    """
    username = RestrictedField(IsAuthenticated)
    password = RestrictedField(IsAuthenticated)

    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')


class Users(ViewSet):
    """
    Users for Optimum
    Purpose: Allow a user to communicate with the database to GET PUT POST and DELETE Users.
    Methods: GET PUT(id) POST
    """

    def retrieve(self, request, pk=None):
        
        """Handle GET requests for single reader
        Purpose: Allow a user to communicate with the database to retrieve  one user
        Methods:  GET
        Returns:
            Response -- JSON serialized reader instance
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    @permission_classes([IsAuthenticatedOrReadOnly])
    def list(self, request):
        """Handle GET requests to user resource"""
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Handle PUT requests for a user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)