from django.urls import path
#from .views import follow_user, unfollow_user

from rest_framework.routers import DefaultRouter
from django.urls import include, path

from auth_user import views

app_name = 'user'

router = DefaultRouter()
router.register('account-user', views.AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('user/follow/<str:username>/', views.follow_userr, name='follow-user'),
    path('user/unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('user/feed/', views.feed_user, name='feed_user'),

]
