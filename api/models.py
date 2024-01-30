from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class CustomeUserManager(BaseUserManager):
  """Manager for user model"""
  def create_user(self, name, email, password=None):
    """Create staff user"""
    if not email:
      raise ValueError("User must have both email address and password")
    
    email = self.normalize_email(email)
    user = self.model(name=name, email=email)

    user.set_password(password)
    user.is_staff=True
    user.save(using=self._db)

    return user

  def create_superuser(self, name, email, password):
    """Create admin user"""
    user = self.create_user(name, email, password)

    user.is_superuser = True
    user.save(using=self._db)

    return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
  """User Model of the system"""
  email = models.EmailField(max_length=250, unique=True)
  name = models.CharField(max_length=50)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=True)
  create_date = models.DateTimeField(null=True, default=timezone.now)
  update_date = models.DateTimeField(null=True, default=timezone.now)

  objects = CustomeUserManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name"]

  def __str__(self):
    return self.name