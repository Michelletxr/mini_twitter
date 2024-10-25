from rest_framework import serializers
from auth_user.models import UserAccount
from post.models import Post

class PostLikeSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    hashtags = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('is_deleted', 'created_at', 'updated_at', 'likes_count', 'user', 'comments')
    
    def create(self, validated_data):
        print("validate data", validated_data)
        return super().create(validated_data)
    
    def validate(self, attrs):
        attrs["user"] =  UserAccount.objects.get(id=self.context["request"].user.id)
        return attrs