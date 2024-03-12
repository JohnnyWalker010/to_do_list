from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = "to_do_list_app"

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    task_done = models.BooleanField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = "to_do_list_app"

    def __str__(self):
        return self.content
