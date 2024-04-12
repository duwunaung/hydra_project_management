from django.urls import path
from . import views

app_name = "backbone"

urlpatterns = [
    path ("", views.index, name="index")
]
