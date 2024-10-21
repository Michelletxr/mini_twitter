from django.shortcuts import render
from rest_framework import viewsets
from post.serializers import PostLikeSerializer

# Create your views here.

class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = serializer_class.Meta.model.objects.all()