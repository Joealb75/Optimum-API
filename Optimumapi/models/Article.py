# from django.db import models
# from django.conf import settings
# from .ArticleTags import Tags
# from .user import User

# class Article(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tag = models.ManyToManyField(Tags, through='ArticleTags')
#     image = models.ImageField(null=True, blank=True, upload_to="articleImages/")
#     title = models.CharField(max_length=200)
#     article_content = models.TextField()
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.title
