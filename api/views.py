from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from api import serializers, models


class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = serializers.CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = models.CustomUser.objects.all()
