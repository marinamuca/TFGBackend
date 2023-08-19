from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from api.models import UserProfile


class CustomRegistrationSerializer(RegisterSerializer):
    
  profile_type = serializers.ChoiceField(choices=UserProfile.USER_TYPE)

  def custom_signup(self, request, user):
      profile_type = self.validated_data.get('profile_type')
      UserProfile.objects.create(user=user, type=profile_type)
