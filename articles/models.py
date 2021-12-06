from django.contrib.auth import get_user_model
from django.db import models
from deufood.utils import random_filename


class Article(models.Model):

    class Meta:
        ordering = ['-created_at']

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(get_user_model(), related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    thumbnail = models.ImageField(upload_to=random_filename)
    contents = models.TextField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    contents = models.TextField()
