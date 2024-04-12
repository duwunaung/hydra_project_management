from django.urls import path
from . import views

app_name = "todolist"

urlpatterns = [
    path("add-todo/", views.add_todo, name="add-todo"),
    path("<uuid:pk>/", views.todolist, name="todolist"),
    path("<uuid:pk>/edit-todo/", views.edit_todolist, name="edit-todolist"),
    path("<uuid:pk>/delete-todo/", views.delete_todo, name="delete-todolist"),
]
