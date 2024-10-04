from django.urls import path
from .views.tag_views import TagListCreateView, TagDetailApiView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailApiView.as_view(), name='tag-detail'),
]
