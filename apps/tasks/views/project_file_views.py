from rest_framework import generics, status
from rest_framework.response import Response
from apps.tasks.models.project_file import ProjectFile  # Импортируйте вашу модель файла проекта
from apps.tasks.serializers.project_file_serializers import AllProjectFilesSerializer, CreateProjectFileSerializer

class ProjectFileListAPIView(generics.ListCreateAPIView):
    serializer_class = AllProjectFilesSerializer  # Укажите сериализатор для списка файлов

    def get_queryset(self):
        project_name = self.request.query_params.get('project_name')  # Получите имя проекта из параметров запроса
        queryset = ProjectFile.objects.all()  # Получите все файлы проекта

        if project_name:
            queryset = queryset.filter(project__name=project_name)  # Фильтруйте файлы по имени проекта
        return queryset  # Верните отфильтрованный или полный queryset

    def create(self, request, *args, **kwargs):
        serializer = CreateProjectFileSerializer(data=request.data, context={'request': request})  # Сериализуйте данные для создания нового файла
        if serializer.is_valid():
            serializer.save()  # Сохраните новый файл проекта
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Верните созданный файл с статусом 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Верните ошибки валидации с статусом 400
