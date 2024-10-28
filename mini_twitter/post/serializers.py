from rest_framework import serializers
from auth_user.models import UserAccount
from post.models import Post, Hashtag

class PostLikeSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    hashtags_list = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('is_deleted', 'created_at', 'updated_at', 'likes_count', 'user', 'comments', 'hashtags')
    
    def create(self, validated_data):
        print("validate data", validated_data)
        hashtags_data = validated_data.pop('hashtags_list', [])
        post = super().create(validated_data)
        
        for hashtag_name in hashtags_data:
            hashtag = Hashtag.objects.get_or_create(name=hashtag_name)[0]
            if hashtag:
                post.hashtags.add(hashtag)

        return post
    
    def validate(self, attrs):
        attrs["user"] =  UserAccount.objects.get(id=self.context["request"].user.id)
        return attrs