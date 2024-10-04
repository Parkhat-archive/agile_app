import os
from django.core.exceptions import ValidationError

VALID_EXTENSIONS = ['pdf', 'csv', 'doc', 'xlsx']

def validate_file_extension(file_name):
    """Проверяет валидное расширение файла."""
    ext = file_name.split('.')[-1].lower()
    if ext not in VALID_EXTENSIONS:
        raise ValidationError(f"Неверное расширение файла: {ext}. Доступные расширения: {', '.join(VALID_EXTENSIONS)}.")

def validate_file_size(file):
    """Проверяет размер файла (не более 2 MB)."""
    max_size = 2 * 1024 * 1024  # 2 MB
    if file.size > max_size:
        raise ValidationError("Размер файла не должен превышать 2 MB.")

def create_file_path(project_id, file_name):
    """Создает путь для сохранения файла."""
    return os.path.join('uploads', 'projects', str(project_id), file_name)

def save_file(file, file_path):
    """Сохраняет файл по частям."""
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
