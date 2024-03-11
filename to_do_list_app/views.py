from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from to_do_list_app.forms import (
    TaskCreateForm,
    TaskUpdateForm,
    TagCreateForm,
    TagUpdateForm,
)
from to_do_list_app.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "to_do_list_app/tasks_list.html"
    context_object_name = "tasks"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "to_do_list_app/create_task.html"
    success_url = reverse_lazy("to_do_list_app:tasks_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "to_do_list_app/update_task.html"
    success_url = reverse_lazy("to_do_list_app:tasks_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "to_do_list_app/delete_task.html"
    success_url = reverse_lazy("to_do_list_app:tasks_list")


class TaskCompleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.task_done = True
        task.save()
        return redirect("to_do_list_app:tasks_list")


class TaskUndoView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.task_done = False
        task.save()
        return redirect("to_do_list_app:tasks_list")


class TagListView(ListView):
    model = Tag
    template_name = "to_do_list_app/tags_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "to_do_list_app/create_tag.html"
    success_url = reverse_lazy("to_do_list_app:tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagUpdateForm
    template_name = "to_do_list_app/update_tag.html"
    success_url = reverse_lazy("to_do_list_app:tags_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "to_do_list_app/delete_tag.html"
    success_url = reverse_lazy("to_do_list_app:tags_list")
