import os
from django.conf import settings
from django.core.exceptions import ValidationError

# Определите допустимые расширения файлов
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'}

def validate_file_extension(file_name):
    """Проверяет, допустимо ли расширение файла."""
    ext = file_name.split('.')[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f'Недопустимое расширение файла: {ext}. Допустимые расширения: {", ".join(ALLOWED_EXTENSIONS)}.')

def validate_file_size(file):
    """Проверяет размер файла (не больше 5 МБ)."""
    max_size = 5 * 1024 * 1024  # 5 MB
    if file.size > max_size:
        raise ValidationError('Размер файла превышает 5 МБ.')

def create_file_path(instance, filename):
    """Создает уникальный путь для сохранения файла."""
    file_extension = filename.split('.')[-1]
    unique_filename = f"{instance.id}.{file_extension}"  # Уникальное имя файла
    return os.path.join('uploads', unique_filename)  # Путь для сохранения файла

def save_file(file):
    """Сохраняет файл на сервере."""
    file_path = create_file_path(file)  # Создает путь для сохранения
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
