"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from api.views import *
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()

router.register(r'exhibition', ExhibitionViewSet)
router.register(r'illustration', IllustrationViewSet)
router.register(r'user_profile', UserProfileViewSet)
router.register(r'likes', LikesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/change_profile/", ChangeProfileTypeView.as_view(), name="change_profile"),
    path("api/check_like/<int:exhibition_id>/", CheckLikeView.as_view(), name="check_like"),
    path("api/liked_exhibitions/", UserLikedExhibitionsView.as_view(), name="liked_exhibitions"),
    path('api/auth/', include('user_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
