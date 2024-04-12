from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project

@login_required
def projects(request):
    projects = Project.objects.filter(created_by = request.user)
    return render(request, "projects.html", {
        "projects": projects
    })

@login_required
def add_project(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        description = request.POST.get("description", "")
        if name:
            project = Project.objects.create(name = name, description = description, created_by = request.user)
            return redirect("/projects/")
    return render(request, "add_project.html")

@login_required
def detail_project(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk = pk)
    return render(request, "project.html", {
        "project" : project
    })

@login_required
def edit_project(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk = pk)
    if request.method == "POST":
        name = request.POST.get("name", "")
        description = request.POST.get("description", "")
        if name: 
            project.name = name
            project.description = description
            project.save()

            return redirect("/projects/", {
                "project": project
            })

    return render(request, "edit_project.html", {
        "project" : project
    })

@login_required
def delete_project(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk=pk)
    project.delete()
    return redirect("/projects/")