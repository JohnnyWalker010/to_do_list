from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCompleteView,
    TaskUndoView,
)

app_name = "to_do_list_app"

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks_list"),
    path("tasks/create/", TaskCreateView.as_view(), name="create_task"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="update_task"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="create_tag"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="update_tag"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="delete_tag"),
    path("complete_task/<int:pk>/", TaskCompleteView.as_view(), name="complete_task"),
    path("undo_task/<int:pk>/", TaskUndoView.as_view(), name="undo_task"),
]
