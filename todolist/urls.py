from django.urls import path
from . import views

app_name = "todolist"

urlpatterns = [
    path("add-todo/", views.add_todo, name="add-todo"),
    path("todo/<uuid:pk>/", views.todolist, name="todolist"),
    path("todo/<uuid:pk>/edit-todo/", views.edit_todolist, name="edit-todolist"),
    path("todo/<uuid:pk>/delete-todo/", views.delete_todo, name="delete-todolist"),
]
