from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from OptimumAPI.models import OfficeUser
from rest_framework.decorators import action

class OfficeUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = OfficeUser
        fields = ('user', 'phone_number', 'profession',
                  'aboutMe', 'profileImage', 'isAdmin')
        
class OfficeUserViewSet(ViewSet):

    def create(self, request):
        user_data = request.data.pop('user')
        user = User.objects.create(**user_data)
        office_user_data = request.data
        office_user_data['user'] = user.id
        serializer = OfficeUserSerializer(data=office_user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        user.delete()  # Rollback the created user if the OfficeUser creation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            office_user = OfficeUser.objects.get(pk=pk)
            serializer = OfficeUserSerializer(office_user)
            return Response(serializer.data)
        except OfficeUser.DoesNotExist:
            return Response({'error': 'OfficeUser not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            office_user = OfficeUser.objects.get(pk=pk)
            user_data = request.data.pop('user')
            user = office_user.user

            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

            for attr, value in request.data.items():
                setattr(office_user, attr, value)
            office_user.save()

            serializer = OfficeUserSerializer(office_user)
            return Response(serializer.data)
        except OfficeUser.DoesNotExist:
            return Response({'error': 'OfficeUser not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            office_user = OfficeUser.objects.get(pk=pk)
            user = office_user.user
            office_user.delete()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except OfficeUser.DoesNotExist:
            return Response({'error': 'OfficeUser not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        office_users = OfficeUser.objects.all()
        serializer = OfficeUserSerializer(office_users, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_user_id(self, request):
        user_id = request.query_params.get('user_id')
        if user_id is None:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            office_user = OfficeUser.objects.get(user_id=user_id)
            serializer = OfficeUserSerializer(office_user)
            return Response(serializer.data)
        except OfficeUser.DoesNotExist:
            return Response({'error': 'OfficeUser not found'}, status=status.HTTP_404_NOT_FOUND)