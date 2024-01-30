from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta

from api import serializers, models, permissions


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginAPIView(APIView):
  serializer_class = serializers.LoginSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)

    if not serializer.is_valid():
      return Response({"detail": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
    
    username = serializer.validated_data.get("email")
    password = serializer.validated_data.get("password")
    user = authenticate(username=username, password=password)
    if user is None:
      return Response({"detail": "No user found"}, status=status.HTTP_401_UNAUTHORIZED)
    
    token = get_tokens_for_user(user)
    
    response = Response()
    response.set_cookie(
      key="refresh",
      value=token.get("refresh"),
      max_age=timedelta(days=1),
      httponly=True
    )
    access_token = {"access": token.get("access")}
    response.data = access_token
    response.status_code = 200
    return response


class RefreshTokenAPIView(APIView):
  def get(self, request):
    refresh_token = request.COOKIES.get("refresh")
    try:
      if refresh_token is None:
        raise ValueError("Refresh token is not valid")
      token = RefreshToken(refresh_token)
      access_token = {"access": str(token.access_token)}
      return Response(access_token, status=status.HTTP_200_OK)
    except ValueError as error:
      return Response({"detail": repr(error)}, status=status.HTTP_401_UNAUTHORIZED)
    except:
      return Response({"detail": "Something went wrong!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
