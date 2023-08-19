from rest_framework import permissions
from api.models import UserProfile

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True 
    
    return request.user.is_authenticated and obj.artist.id == request.user.id

class IsAuthenticatedCreateOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in ['POST']:
      return request.user.is_authenticated and UserProfile.objects.get(user=request.user).isArtist()
    
    return True