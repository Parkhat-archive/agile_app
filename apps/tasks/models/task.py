from django.db import models
from django.contrib.auth.models import User
from apps.projects.models.project import Project
from apps.tasks.models.tag import Tag
from enum import Enum
from datetime import datetime

# Определяем перечисление для статусов
class Statuses(Enum):
    NEW = 'NEW'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

# Определяем перечисление для приоритетов
class Priority(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=[(status.value, status.name) for status in Statuses], default=Statuses.NEW.value)
    priority = models.CharField(max_length=15, choices=[(priority.value, priority.name) for priority in Priority], default=Priority.MEDIUM.value)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(default=datetime.now)
    assignee = models.ForeignKey(User, related_name='tasks', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}, {self.status}"  # Изменено для отображения формата "название задачи, статус"

    class Meta:
        ordering = ['-deadline']  # Сортировка по дедлайну в порядке убывания
        unique_together = ('name', 'project')  # Уникальность по полям name и project
