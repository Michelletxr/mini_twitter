from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    class Meta:
        model = UserAccount
        fields = '__all__'
    
    def get_followers_count(self, instance: UserAccount):
        return instance.author.followers.all()

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