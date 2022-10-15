from django.contrib import admin

# Register your models here.
from social.models import Post, LikePost

admin.site.register(Post)
admin.site.register(LikePost)