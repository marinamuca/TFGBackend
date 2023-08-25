from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from api.models import UserProfile
from django.contrib.auth import get_user_model
from api.serializers import UserProfileSerializer


class CustomRegistrationSerializer(RegisterSerializer):
  is_artist = serializers.BooleanField()

  def custom_signup(self, request, user):
      is_artist = self.validated_data.get('is_artist')
      UserProfile.objects.create(user=user, is_artist=is_artist)


class CustomUserDetailSerializer(serializers.ModelSerializer):
    profile_data = UserProfileSerializer(read_only = True, source="profile")
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'profile_data')

class GetUserByIDSerializer(serializers.ModelSerializer):
    profile_data = UserProfileSerializer(read_only = True, source="profile")
    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_data')