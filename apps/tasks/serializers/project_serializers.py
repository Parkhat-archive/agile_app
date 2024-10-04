from rest_framework import serializers
from apps.tasks.models.project import Project

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'created_at', 'count_of_files']
