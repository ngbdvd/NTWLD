from rest_framework.viewsets import ModelViewSet
from .serializers import ContentSerializer
from ..models import Content

class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
