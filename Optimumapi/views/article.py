from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from OptimumAPI.models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#! ------------------------ Article Stuff
class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleViewSet(ViewSet):

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, context={'request': request})
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @permission_classes([IsAuthenticatedOrReadOnly])
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        return Response(serializer.data)
#! ------------------------ Tag Stuff

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagViewSet(ViewSet):

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, context={'request': request})
            return Response(serializer.data)
        except Tag.DoesNotExist:
            return Response({'error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response({'error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response({'error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @permission_classes([IsAuthenticatedOrReadOnly])
    def list(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True, context={'request': request})
        return Response(serializer.data)

#! ------------------------ ArticleTag Stuff

class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'

class ArticleTagViewSet(ViewSet):
    def create(self, request):
        serializer = ArticleTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            article_tag = ArticleTag.objects.get(pk=pk)
            serializer = ArticleTagSerializer(article_tag, context={'request': request})
            return Response(serializer.data)
        except ArticleTag.DoesNotExist:
            return Response({'error': 'ArticleTag not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            article_tag = ArticleTag.objects.get(pk=pk)
            serializer = ArticleTagSerializer(article_tag, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ArticleTag.DoesNotExist:
            return Response({'error': 'ArticleTag not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            article_tag = ArticleTag.objects.get(pk=pk)
            article_tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ArticleTag.DoesNotExist:
            return Response({'error': 'ArticleTag not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @permission_classes([IsAuthenticatedOrReadOnly])
    def list(self, request):
        article_tags = ArticleTag.objects.all()
        serializer = ArticleTagSerializer(article_tags, many=True, context={'request': request})
        return Response(serializer.data)