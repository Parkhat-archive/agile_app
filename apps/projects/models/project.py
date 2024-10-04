from django.db import models

class ProjectFile(models.Model):
    file_name = models.CharField(max_length=120)
    file_path = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.file_name


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(ProjectFile, related_name='projects', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def count_of_files(self):
        return self.files.count()
