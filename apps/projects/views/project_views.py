

from rest_framework import generics
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
from apps.projects.models.project import Project
from apps.projects.serializers.project_serializers import AllProjectsSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = AllProjectsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if date_from and date_to:

            date_from = make_aware(datetime.strptime(date_from, '%Y-%m-%d'))
            date_to = make_aware(datetime.strptime(date_to, '%Y-%m-%d'))
            queryset = queryset.filter(created_at__range=(date_from, date_to))

        return queryset

