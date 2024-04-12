from django.urls import path
from . import views
app_name = "task"

urlpatterns = [
    path("add-task/", views.add_task, name="add-task"),
    path("<uuid:pk>/", views.detail_task, name="detail-task"),
    path("<uuid:pk>/edit-task/", views.edit_task, name="edit-task"),
    path("<uuid:pk>/delete-task", views.delete_task, name="delete-task")

]
