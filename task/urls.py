from django.urls import path
from . import views
app_name = "task"

urlpatterns = [
    path("task/add-task/", views.add_task, name="add-task"),
    path("task/<uuid:pk>/", views.detail_task, name="detail-task"),
    path("task/<uuid:pk>/edit-task/", views.edit_task, name="edit-task"),
    path("task/<uuid:pk>/delete-task", views.delete_task, name="delete-task")

]
