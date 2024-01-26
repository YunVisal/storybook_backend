from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api import views

router = DefaultRouter()
router.register("user", viewset=views.UserViewSet)

urlpatterns = [
  path("login", views.CustomTokenObtainPairView.as_view(), name='login'),
  path("refresh", TokenRefreshView.as_view(), name='refresh'),
  path("", include(router.urls))
]