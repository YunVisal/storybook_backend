from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from api import views


router = DefaultRouter()
router.register("user", viewset=views.UserViewSet)

urlpatterns = [
  path('schema/', SpectacularAPIView.as_view(), name='schema'),
  path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
  path("login", views.LoginAPIView.as_view(), name='login'),
  path("refresh", views.RefreshTokenAPIView.as_view(), name='refresh'),
  path("", include(router.urls))
]