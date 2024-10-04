from rest_framework import serializers
from apps.tasks.models.project_file import ProjectFile  # Импортируйте вашу модель файла проекта
from .upload_file_helpers import validate_file_extension, validate_file_size, create_file_path, save_file

class AllProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['id', 'file_name', 'project']

class CreateProjectFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)  # Добавляем поле для загрузки файла

    class Meta:
        model = ProjectFile
        fields = ['file_name', 'file', 'project']  # Убедитесь, что project также включен, если необходимо

    def validate_file_name(self, value):
        # Проверка на наличие символов из таблицы ASCII
        if not all(ord(c) < 128 for c in value):
            raise serializers.ValidationError("Имя файла должно содержать только символы ASCII.")
        validate_file_extension(value)  # Проверка на расширение файла
        return value

    def create(self, validated_data):
        file = validated_data.pop('file')  # Получаем файл из validated_data
        project_id = validated_data.pop('project')  # Получаем project из validated_data

        validate_file_size(file)  # Проверка на размер

        # Создание пути для сохранения файла
        file_path = create_file_path(project_id, validated_data['file_name'])
        save_file(file, file_path)  # Сохранение файла

        # Создание объекта файла проекта
        project_file = ProjectFile.objects.create(file_name=validated_data['file_name'], project_id=project_id)
        return project_file
