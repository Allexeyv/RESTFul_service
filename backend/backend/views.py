from backend.backend.models import Publication, Category
from rest_framework import viewsets
from backend.backend.serializers import PublicationSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated


class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Publication to be viewed or edited.
    """
    queryset = Publication.objects.all().order_by('created_at')
    serializer_class = PublicationSerializer
    permission_classes = (IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
