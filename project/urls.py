from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("", views.projects, name="projects"),
    path("create-project/", views.add_project, name="create-project"),
    path("<uuid:pk>/", views.detail_project, name="detail-project"),
    path("<uuid:pk>/edit/", views.edit_project, name="edit-project"),
    path("<uuid:pk>/delete/", views.delete_project, name="delete-project"),
]
