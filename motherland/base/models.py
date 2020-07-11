from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Post's author"
    )
    date = models.DateTimeField(verbose_name="Post creation datetime")
    title = models.TextField(verbose_name="Post's title")
    content_raw = models.TextField(verbose_name="Post's markdown markup")
    comments = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Comments under post"
    )
    rating = models.IntegerField(verbose_name="Rating of post")
    blog = models.BooleanField(verbose_name="Post from blog or not")


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Author of the comment"
    )
    to = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Under which Post this comment leaved"
    )
    datetime = models.DateTimeField(verbose_name="Comment creation datetime")
    content_raw = models.TextField(verbose_name="Comment's markdown markup")
    rating = models.IntegerField(verbose_name="Rating of comment")


class BaseUser(AbstractUser):
    rating = models.IntegerField(verbose_name="User's rating")
    posts = models.ManyToManyField(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Posts of the User"
    )
    comments = models.ManyToManyField(
        Comment,
        on_delete=models.CASCADE,
        verbose_name="Comments of the User"
    )
