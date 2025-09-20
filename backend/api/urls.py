from rest_framework.routers import DefaultRouter
from ntwld.api.urls import content_router
from django.urls import path, include

router = DefaultRouter()

#
router.registry.extend(content_router.registry)

urlpatterns = [
    path('', include(router.urls))
]