from django.urls import path
from .views.tag_views import TagListCreateView, TagDetailApiView
from .views.project_views import ProjectDetailAPIView
from .views.project_file_views import ProjectFileListAPIView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailApiView.as_view(), name='tag-detail'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),  # Новый эндпоинт для проектов
    path('projects/files/', ProjectFileListAPIView.as_view(), name='project-file-list-create'),  # Новый эндпоинт для файлов проекта
]
