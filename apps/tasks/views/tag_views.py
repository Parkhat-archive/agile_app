from rest_framework import generics
from apps.tasks.models.tag import Tag
from apps.tasks.serializers.tag_serializers import TagSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
