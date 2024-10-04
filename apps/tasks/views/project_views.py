from rest_framework import generics, status
from rest_framework.response import Response
from apps.tasks.models.project import Project  # Импортируйте вашу модель проекта
from ..serializers.project_serializers import ProjectDetailSerializer  # Импортируйте ваш сериализатор

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()  # Получите все проекты
    serializer_class = ProjectDetailSerializer  # Укажите ваш сериализатор

    def get(self, request, pk):
        project = self.get_object()  # Получите конкретный проект
        serializer = self.get_serializer(project)  # Сериализуйте проект
        return Response(serializer.data)  # Верните данные проекта

    def put(self, request, pk):
        project = self.get_object()  # Получите конкретный проект
        serializer = self.get_serializer(project, data=request.data, partial=True)  # Обновите проект частично
        if serializer.is_valid():
            serializer.save()  # Сохраните обновленный проект
            return Response(serializer.data)  # Верните обновленные данные
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Верните ошибки валидации

    def delete(self, request, pk):
        project = self.get_object()  # Получите конкретный проект
        project.delete()  # Удалите проект
        return Response(status=status.HTTP_204_NO_CONTENT)  # Верните статус 204
