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
        
class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]

class CheckLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, exhibition_id):
        user_profile = request.user.profile
        try:
            like = Likes.objects.get(exhibition_id=exhibition_id, user_profile=user_profile)
            return Response({'has_like': True, 'like': like.id}, status=status.HTTP_200_OK)
        except Likes.DoesNotExist:
            return Response({'has_like': False}, status=status.HTTP_200_OK)
        
class UserLikedExhibitionsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_profile = request.user.profile
        liked_exhibition_ids = Likes.objects.filter(user_profile=user_profile).values_list('exhibition_id', flat=True)
        exhibitions = Exhibition.objects.filter(id__in=liked_exhibition_ids)
        serializer = ExhibitionSerializer(exhibitions, many=True)
        return Response({'exhibitions': serializer.data}, status=status.HTTP_200_OK)