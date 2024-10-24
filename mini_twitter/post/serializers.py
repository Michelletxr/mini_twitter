from rest_framework import serializers
from auth_user.models import UserAccount
from auth_user.serializers import UserAccountSerializer
from post.models import Post

class PostLikeSerializer(serializers.ModelSerializer):
    #user = UserAccountSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('is_deleted', 'created_at', 'updated_at', 'likes_count', 'user' )
    def create(self, validated_data):
        user = UserAccount.objects.get(id=self.context["request"].user.id)
        print("USER", user, self.context["request"].user.id)
        validated_data['user'] = user
        return super().create(validated_data)