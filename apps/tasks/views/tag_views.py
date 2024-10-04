from rest_framework import generics, status
from rest_framework.response import Response
from apps.tasks.models.tag import Tag
from ..serializers.tag_serializers import TagSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request):
        tags = self.get_queryset()
        serializer = self.get_serializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, pk):
        tag = self.get_object()
        serializer = self.get_serializer(tag)
        return Response(serializer.data)

    def put(self, request, pk):
        tag = self.get_object()
        serializer = self.get_serializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = self.get_object()
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
