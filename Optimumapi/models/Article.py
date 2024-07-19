from django.db import models
from django.conf import settings
from .Tags import Tags

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="articleImages/")
    title = models.CharField(max_length=200)
    article_content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
