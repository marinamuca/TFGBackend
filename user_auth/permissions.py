from rest_framework import permissions
from api.models import UserProfile, Exhibition, Illustration

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True 
    
    return request.user.is_authenticated and obj.artist.id == request.user.id
  
class IsExhibitionOwnerOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True

    if request.method in ['POST']:
      exhibition = Exhibition.objects.get(id=request.data['exhibition'])
      return (request.user.is_authenticated and exhibition.artist.id == request.user.id) 
    
    return request.user.is_authenticated
  
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    exhibition = Illustration.objects.get(id=view.kwargs['pk']).exhibition
    return (request.user.is_authenticated and exhibition.artist.id == request.user.id)

class IsAuthenticatedCreateOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in ['POST']:
      return request.user.is_authenticated and UserProfile.objects.get(user=request.user).is_artist
    
    return True