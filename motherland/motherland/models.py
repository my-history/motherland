from django.db import models
from django.contrib.auth.models import User


class BaseUser(User):
    rating = models.IntegerField(verbose_name="User's rating")
    # posts = None  # many-to-many to Post
    # comments = None  # many-to-many to Comment


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    # author = None  # User
    date = models.DateTimeField(verbose_name="Post creation datetime")
    title = models.TextField(verbose_name="Post's title")
    content_raw = models.TextField(verbose_name="Post's markdown markup")
    # comments = None  # many-to-many к Comment
    rating = models.IntegerField(verbose_name="Rating of post")
    blog = models.BooleanField(verbose_name="Post from blog or not")
