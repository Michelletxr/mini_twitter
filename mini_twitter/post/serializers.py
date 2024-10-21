from rest_framework import serializers
from post.models import Post

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'