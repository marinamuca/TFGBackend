from django.shortcuts import render
from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status, viewsets
from dj_rest_auth.serializers import TokenSerializer
from .serializers import CustomUserDetailSerializer, GetUserByIDSerializer
from django.contrib.auth import get_user_model


class CustomLoginView(LoginView):
  def get_response(self):
    serializer = TokenSerializer(instance=self.token, context={'request': self.request})
    user = self.user
    user_serializer = CustomUserDetailSerializer(user)

    response = {
        'token': serializer.data.get('key'),
        'user': user_serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = GetUserByIDSerializer