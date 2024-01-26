from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("user", viewset=views.UserViewSet)

urlpatterns = [
  path("login", views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path("", include(router.urls))
]