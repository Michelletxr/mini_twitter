from django.db import models
# Create your models here.
# models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
   # comments = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"
    
class Comment(models.Model):
    pass

