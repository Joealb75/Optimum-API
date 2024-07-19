from django.db import models
from .Article import Article
from .Tags import Tags

class ArticleTags(models.Model):
    tagID = models.ForeignKey(Tags, on_delete=models.CASCADE)
    articleID = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag.tag} - {self.article.title}"
