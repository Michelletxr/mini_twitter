from rest_framework.routers import DefaultRouter
from django.urls import include, path

from post import views

app_name = 'post'

router = DefaultRouter()
router.register('like-posts', views.PostLikeViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]