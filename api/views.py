from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from user_auth.permissions import IsAuthenticatedCreateOnly, IsOwnerOrReadOnly, IsExhibitionOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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
    permission_classes = [IsExhibitionOwnerOrReadOnly]

class ChangeProfileTypeView (APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        user_profile = get_object_or_404(UserProfile, user=user.pk)

        if user_profile.is_artist:
            user_profile.is_artist=False
            Exhibition.objects.filter(artist=user_profile).delete()
        else:
            user_profile.is_artist=True

        user_profile.save()
        return Response(status=status.HTTP_200_OK)
        