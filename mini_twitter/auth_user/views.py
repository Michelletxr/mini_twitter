from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from mini_twitter.settings import CACHE_TTL
from post.models import Post


from .serializers import UserAccountSerializer
from .models import UserAccount

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_userr(request, username):
    """Seguir um usuário"""
    user_to_follow = get_object_or_404(UserAccount, username=username)
    request.user.follow(user_to_follow)
    return Response({"detail": f"Você seguiu {user_to_follow.username}"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, username):
    """Deixar de seguir um usuário"""
    user_to_unfollow = get_object_or_404(UserAccount, username=username)
    request.user.unfollow(user_to_unfollow)
    return Response({"detail": f"Você deixou de seguir {user_to_unfollow.username}"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
#@cache_page(CACHE_TTL)
def feed_user(request):
    """feed do usuário."""
    user = request.user
    cache_key = f"user_feed_{user.id}"
     # Tenta obter o feed do cache
    feed_cache = cache.get(cache_key)
    if not feed_cache:
       
        following_users = user.following.all()
        # Ordena por data de criação (mais recentes primeiro)
        feed = Post.objects.filter(user__in=following_users) | Post.objects.filter(user=user).order_by('-updated_at')
        feed_data = [{'user': post.user.username, 'content': post.content, 'created_at': post.created_at} for post in feed]
        # Armazena o feed no cache
        cache.set(cache_key, feed_data, timeout=CACHE_TTL)
    
    return Response(feed_data)

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = UserAccountSerializer
    queryset = serializer_class.Meta.model.objects.all()
    pass
    
    #terminar rotas 
    #terminar funcinalidades principais
    #adicionar paginação
    #adicionar cache
    #rota de login customizada
