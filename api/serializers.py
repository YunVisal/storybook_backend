from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import CustomUser


class LoginSerializer(serializers.Serializer):
  """Serializer for login"""
  email = serializers.CharField()
  password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
  """Serializer for User model"""
  class Meta:
    model = CustomUser
    fields = ("id", "name", "email", "password", "is_superuser", "create_date", "update_date")
    extra_kwargs = {
      "password": {
        "write_only": True
      },
      "is_superuser": {
        "read_only": True
      },
      "create_date": {
        "read_only": True
      },
      "update_date": {
        "read_only": True
      }
    }
  
  def create(self, validated_data):
    """Create new user"""
    user = CustomUser.objects.create_user(
      name=validated_data["name"],
      email=validated_data["email"],
      password=validated_data["password"]
    )
    return user
  
  def update(self, instance, validated_data):
    if 'password' in validated_data:
      password = validated_data.pop('password')
      instance.set_password(password)
    return super().update(instance, validated_data)