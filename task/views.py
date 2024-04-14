from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project.models import Project
from todolist.models import Todolist
from .models import Task


@login_required
def add_task(request, project_id, todolist_id):
    project = Project.objects.filter(
        created_by=request.user
    ).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    if request.method == "POST":
        name = request.POST.get("name", "")
        task = Task.objects.create(
            project=project, created_by=request.user, todolist=todolist, name=name)
        return redirect(f"/projects/{project_id}/todo/{todolist_id}/")
    return render(request, "add_task.html", {
        "todolist": todolist
    })


@login_required
def detail_task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(todolist=todolist).get(pk=pk)

    if request.GET.get("is_done", "") == "yes":
        task.is_done = True
        task.save()

    if request.GET.get("is_done", "") == "no":
        task.is_done = False
        task.save()

    return render(request, "task.html", {
        "task": task
    })


@login_required
def edit_task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(
        created_by=request.user
    ).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(todolist=todolist).get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("name", "")
        if name:
            task.name = name

        task.save()
        print(f"/projects/{project_id}/{todolist_id}/{pk}")
        return redirect(f"/projects/{project_id}/todo/{todolist_id}/task/{pk}")

    return render(request, "edit_task.html", {
        "task": task,
        "todolist": todolist
    })

@login_required
def delete_task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(todolist=todolist).get(pk=pk)
    task.delete()
    return redirect(f"/projects/{project_id}/todo/{todolist_id}/")
