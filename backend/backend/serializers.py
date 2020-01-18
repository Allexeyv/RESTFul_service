from backend.backend.models import Publication, Category
from rest_framework.serializers import ModelSerializer


class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'