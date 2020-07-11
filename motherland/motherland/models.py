from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    # author = None  # User
    date = models.DateTimeField(verbose_name="Datetime of creating post")
    title = models.TextField(verbose_name="Post's title")
    content_raw = models.TextField(verbose_name="Post's markdown markup")
    # comments = None  # many-to-many к Comment
    rating = models.IntegerField(verbose_name="Rating of post")
