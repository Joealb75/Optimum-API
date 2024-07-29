from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Users

    Arguments:
        serializers
    """
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