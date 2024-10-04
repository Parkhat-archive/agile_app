

from django.urls import path
from apps.projects.views.project_views import ProjectListCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
]
