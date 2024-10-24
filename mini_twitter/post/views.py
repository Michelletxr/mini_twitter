from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from mini_twitter.settings import CACHE_TTL
from post.models import Post
from mini_twitter.utils import CustomPagination
from post.serializers import PostLikeSerializer

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(CACHE_TTL)
def get_posts_cacheable(request):
    posts = Post.objects.all()
      # Serializa os posts
    #serializer = PostLikeSerializer(posts, many=True)
    return Response(posts)

class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('-created_at')
    pagination_class = CustomPagination


