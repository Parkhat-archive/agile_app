from django.db import models
from apps.projects.models.project import Project  # Импортируем модель Project

class ProjectFile(models.Model):
    file_name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='project_files', on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name
