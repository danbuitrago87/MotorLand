from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def hello(request,username):
    print(username)
    return HttpResponse("Hello %s" % username)

def about(request):
    return HttpResponse("About")

def index(request):
    return HttpResponse("Index page")

def projects(request):
    projects=list (Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    task=Task.objects.get(title=title)
    return HttpResponse("task: %s" %task.title)