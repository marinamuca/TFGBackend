from rest_framework import serializers
from .models import *

class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustration
        fields = '__all__'

        
class ExhibitionSerializer(serializers.ModelSerializer):
    illustrations = IllustrationSerializer(read_only = True, many = True, source = "illustration_set")
    class Meta:
        model = Exhibition
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    exhibitions = ExhibitionSerializer(read_only = True, many = True, source = "exhibition_set")
    class Meta:
        model = UserProfile
        exclude = ['user']