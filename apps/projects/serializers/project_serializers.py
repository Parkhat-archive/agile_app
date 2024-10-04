from rest_framework import serializers
from apps.projects.models.project import Project

class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at']