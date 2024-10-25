from django.db import models
from django.db import models
from auth_user.models import UserAccount

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    total_references = models.IntegerField(default=0)

    def __str__(self):
        return f"#{self.name}"
    
class Comment(models.Model):
    pass

class Post(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    hashtags = models.ManyToManyField(Hashtag, related_name='posts', blank=True)
    comments = models.ManyToManyField(Comment, related_name='posts', blank=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"
    


