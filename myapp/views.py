from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Project,Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTaskForm

# Create your views here.
def queonda(req, nombre):
    print(nombre)
    return HttpResponse("Que onda %s" % nombre)

def about(req):
    return render(req,'about.html')

def index(req):
    title = 'Django Course!!'
    return render(req,'index.html',{
        'title':title
    })


def projects(req):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)


def tasks(req,id):
    #task =  Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s ' % task.title)


def proyectos(req):
    projects = Project.objects.all()
    return render(req,'projects.html',{
        'projects':projects
    })



def tareas(req):
    tasks = Task.objects.all()
    return render(req,'tareas.html',{
        'tasks':tasks
    })

def create_task(req):

    #print(req.GET)


    if req.method == 'GET':
        return render(req,'create_task.html',{
        'form': CreateNewTaskForm()
    })

    else:
        Task.objects.create(title=req.GET['title'], description = req.GET['description'],project_id=2)
        return redirect('/tareas')



