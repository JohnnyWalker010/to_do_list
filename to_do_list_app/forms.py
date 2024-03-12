from django.forms import ModelForm

from to_do_list_app.models import Task, Tag


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "task_done", "tags"]


class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "task_done", "tags"]


class TagCreateForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TagUpdateForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
