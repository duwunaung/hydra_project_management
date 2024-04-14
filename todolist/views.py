from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project.models import Project

from .models import Todolist


@login_required
def add_todo(request, project_id):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)

    if request.method == "POST":
        name = request.POST.get("name", "")
        description = request.POST.get("description", "")
        if name:
            todolist = Todolist.objects.create(
                project=project, name=name, description=description, created_by=request.user)

            return redirect(f"/projects/{project_id}/")

    return render(request, "add_todo.html", {
        "project": project
    })


@login_required
def todolist(request, project_id, pk):
    project = Project.objects.filter(
        created_by=request.user
    ).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    return render(request, "detail_todo.html", {
        "project": project,
        "todolist": todolist
    })

@login_required
def edit_todolist(request, project_id, pk):
    project = Project.objects.filter(
        created_by=request.user
    ).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("name", "")
        description = request.POST.get("description", "")
        if name:
            todolist.name = name
            todolist.description = description
            todolist.save()
            return redirect(f"/projects/{project_id}/{pk}")
        
    return render(request, "edit_todo.html", {
        "project" : project,
        "todolist": todolist

    })

@login_required
def delete_todo(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todo=Todolist.objects.filter(project=project).get(pk=pk)
    todo.delete()
    return redirect(f"/projects/{project_id}/")