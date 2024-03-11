from django.views.generic import ListView

from django.shortcuts import render

from to_do_list_project.to_do_list_app.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
