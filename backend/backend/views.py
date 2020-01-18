from backend.backend.models import Publication, Category
from rest_framework import viewsets
from backend.backend.serializers import PublicationSerializer, CategorySerializer


class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Publication.objects.all().order_by('created_at')
    serializer_class = PublicationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer
