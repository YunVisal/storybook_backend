from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from api import serializers, models, permissions


class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = serializers.CustomTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = models.CustomUser.objects.all()
  permission_classes = (permissions.IsOwnProfile, )

  def list(self, request):
    if request.user.id is None:
      return Response({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not request.user.is_superuser:
      return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
    
    queryset = models.CustomUser.objects.all()
    serializer = serializers.UserSerializer(queryset, many=True)
    return Response(serializer.data)
