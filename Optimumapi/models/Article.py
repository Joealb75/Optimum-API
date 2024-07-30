from django.db import models
from django.conf import settings
from .user import User

class Tag(models.Model):
    tag = models.CharField(max_length=100)

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, through='ArticleTag')
    image = models.ImageField(null=True, blank=True, upload_to="articleImages/")
    title = models.CharField(max_length=200)
    article_content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    adminApproved = models.BooleanField(default=False)

class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)



