from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    # author = None  # User
    date = models.DateTimeField()
    title = models.TextField()
    content_raw = models.TextField()
    # comments = None  # many-to-many к Comment
    rating = models.IntegerField()
