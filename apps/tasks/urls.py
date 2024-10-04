# apps/tasks/urls.py

from django.urls import path
from .views.tag_views import TagListCreateView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
]
