from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from OptimumAPI.models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class ConsultationViewSet(ViewSet):

    def create(self, request):
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            consultation = Consultation.objects.get(pk=pk)
            serializer = ConsultationSerializer(consultation)
            return Response(serializer.data)
        except Consultation.DoesNotExist:
            return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            consultation = Consultation.objects.get(pk=pk)
            serializer = ConsultationSerializer(consultation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Consultation.DoesNotExist:
            return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            consultation = Consultation.objects.get(pk=pk)
            consultation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Consultation.DoesNotExist:
            return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        consultations = Consultation.objects.all()
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)
