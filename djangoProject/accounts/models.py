from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, default='0000000000')
    userId = models.IntegerField(default=1)
    createdOn = models.DateTimeField(default=datetime.now())
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
