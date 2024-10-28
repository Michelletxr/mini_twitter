from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from mini_twitter.utils import CustomPagination
from mini_twitter.settings import CACHE_TTL
from post.models import Post
from post.serializers import PostLikeSerializer


from .serializers import LoginSerializer, UserAccountSerializer
from .models import UserAccount

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_userr(request, username):
    """Seguir um usuário"""
    user_to_follow = get_object_or_404(UserAccount, username=username)
    user = UserAccount.objects.get(id=request.user.id)
    user.follow(user_to_follow)
    user_to_follow.total_followers = user_to_follow.total_followers + 1
    user_to_follow.save(update_fields=['total_followers'])
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
        # Armazena o feed no cache
        cache.set(cache_key, list(feed.values()), timeout=CACHE_TTL)
        # Tenta obter o feed do cache novamente
        feed_cache = cache.get(cache_key)
    
    return Response(data={"posts":feed_cache})

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = UserAccountSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('username')
    pagination_class = CustomPagination
   

    # Definir permissões para as ações
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Permitir acesso a todos na rota de listagem
            return [AllowAny()]
       
        return [IsAuthenticated()]

    #DOCKER
    #CELERY E EMAIL



class LoginViewSet(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
