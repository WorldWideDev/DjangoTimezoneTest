from django.db import models
from home.models import User
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    
    # who made the post!
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    # timestamp!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # likes!
    # comments