from time import timezone
from django.db import models
from Feeds.models import Posts
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class comments(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
