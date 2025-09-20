from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()
# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Username")
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_picture', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user}"
    
class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='content_images', blank=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    like = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    bookmarks = models.IntegerField(default=0)
    category = models.CharField(blank=True)

    def __str__(self):
        return f"{self.user} {self.text} {self.created_at}"
    
class Like(models.Model):
    content_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"

class Bookmarks(models.Model):
    content_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}"
    
class Views(models.Model):
    content_id = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} {self.comment}"
    
class Vote(models.Model):
    content_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"