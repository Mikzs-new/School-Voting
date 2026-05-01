from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

# V1
router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='students')

urlpatterns = [
    path('v1', include(router)),
]