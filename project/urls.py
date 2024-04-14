from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("", views.projects, name="projects"),
    path("create-project/", views.add_project, name="create-project"),
    path("<uuid:pk>/", views.detail_project, name="detail-project"),
    path("<uuid:pk>/edit/", views.edit_project, name="edit-project"),
    path("<uuid:pk>/delete/", views.delete_project, name="delete-project"),
    path("<uuid:project_id>/attachment/add_attachment/", views.add_attachment, name="add-attachment"),
    path("<uuid:project_id>/attachment/<uuid:pk>/delete/", views.delete_attachment, name="delete-attachment"),
    path("<uuid:project_id>/note/add_note/", views.add_note, name="add-note"),
    path("<uuid:project_id>/note/<uuid:pk>/delete/", views.delete_note, name="delete-note"),
    path("<uuid:project_id>/note/<uuid:pk>/", views.detail_note, name="detail-note"),
    path("<uuid:project_id>/note/edit_note/<uuid:pk>/", views.edit_note, name="edit-note")

]
