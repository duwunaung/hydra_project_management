import uuid
from django.db import models
from account.models import User
from project.models import Project
from todolist.models import Todolist

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    todolist = models.ForeignKey(Todolist, related_name="tasks", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name