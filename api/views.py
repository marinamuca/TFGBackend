from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from user_auth.permissions import IsAuthenticatedCreateOnly, IsOwnerOrReadOnly


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [IsAuthenticatedCreateOnly, IsOwnerOrReadOnly]
    
class IllustrationViewSet(viewsets.ModelViewSet):
    queryset = Illustration.objects.all()
    serializer_class = IllustrationSerializer