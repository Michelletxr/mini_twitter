from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.cache import cache_page
from rest_framework import status, viewsets
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
    serializer = PostLikeSerializer(posts, many=True)
    return Response(Response(data={"posts_cache":serializer.data}))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    try:
        
        post = Post.objects.get(id=post_id)
        likes_count_up = post.likes_count + 1
        post.likes_count = likes_count_up
        post.save(update_fields=['likes_count'])
    
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostLikeSerializer(post)
    #print(serializer.data)
    return Response(data={"post": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deslike_post(request, post_id):
    try:
        
        post = Post.objects.get(id=post_id)
        likes = post.likes_count
        if likes > 0:
            likes_count_down = likes - 1
            post.likes_count = likes_count_down
            post.save()
    
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostLikeSerializer(post)
    return Response(data={"post": serializer.data}, status=status.HTTP_200_OK)
    

class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('-created_at')
    pagination_class = CustomPagination

    def list(self, request):
        query = request.GET.get('hashtag_name', '')
        print("query", query)
        posts = Post.objects.filter(
            Q(hashtags__name__icontains=query)
        )
        serializer = PostLikeSerializer(posts, many=True)
        return Response(serializer.data)




