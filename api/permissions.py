from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnProfile(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method == 'POST':
      return True
    
    return request.user.id == obj.id