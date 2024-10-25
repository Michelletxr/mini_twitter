from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    followers = serializers.StringRelatedField(many=True, read_only=True)
    following = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = UserAccount
        exclude = ('last_login', 'is_active', 'is_staff', 'is_superuser')
        read_only_fields = ('groups', 'user_permissions', 'followers')

    def get_followers_count(self, instance: UserAccount):
        return instance.followers.count()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                 raise serializers.ValidationError("Credenciais incorretas.")
        data['user'] = user
        return data