import uuid
from mimetypes import guess_type

from django.contrib.auth.models import User
from django.http import request
from django.utils import timezone
from django.db import models
from uuid import uuid4
from datetime import datetime

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.FileField(upload_to='user_posts')
    write = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def media_type_(self):
        type_tuple = guess_type(self.image.url, strict=True)
        if type_tuple[0].__contains__("image"):
            return "image"
        elif type_tuple[0].__contains__("video"):
            return "video"
    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

