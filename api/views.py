from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    
class IllustrationViewSet(viewsets.ModelViewSet):
    queryset = Illustration.objects.all()
    serializer_class = IllustrationSerializer