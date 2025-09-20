from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet

content_router = DefaultRouter()
content_router.register(r'content', ContentViewSet)


urlpatterns = content_router.urls