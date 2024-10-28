from rest_framework.routers import DefaultRouter
from django.urls import include, path

from post import views

app_name = 'post'

router = DefaultRouter()
router.register('like-posts', views.PostLikeViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    #testar rota de cache
    path('posts-cache', views.get_posts_cacheable, name='post-cache'),
    path('post-like/<int:post_id>/', views.like_post, name='post-like'),
    path('post-deslike/<int:post_id>/', views.deslike_post, name='post-deslike'),

]