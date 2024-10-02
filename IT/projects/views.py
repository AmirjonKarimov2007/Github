from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
# Projects and Project Details Pages views
def projectsview(request):
    projects = Project.objects.all()

    context = {
        "projects": projects
    }
    return render(request,'projects/projects.html',context)


def projectdetailview(request,id):
    project = Project.objects.get(id=id)
  
    context = {
        "project":project
    }
    return render(request,'projects/single-project.html',context)



# End Projects and Project Details Pages views





# Project Edit Details

def projectadd(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ProjectForm()
    
    context = {
        "form":form
    }
    return render(request,'projects/project_add.html',context)    

def editproject(request,id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form":form
    }
    return render(request,'projects/project_add.html',context)


def deleteproject(request,id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('/')
    

# End Project Details