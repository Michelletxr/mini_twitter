"""
URL configuration for mini_twitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from mini_twitter import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Mini-Twitter API",
      default_version='v1',
      description="Mini-Twitter - API Documentation"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

v1_api_urlpatterns = [
   # path(settings.SITE_PATH, include_api_urls('v1', namespace='api'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auth_user.urls')),
    path('api/', include('post.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

]

