from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.template import loader
from . models import task

# Create your views here.

def index(request):
    #template = loader.get_template("app/index.html")
    db_data = task.objects.all()
    context = {
        "db_data": db_data
    }
    print(db_data)
    #return HttpResponse(template.render(context, request))
    return render(request, "app/index.html", context)

def insert(request):
    task_task = request.POST["task"]
    task_description = request.POST["description"]
    db_data = task(task=task_task, description=task_description)
    db_data.save()
    #print(request.POST["task"])
    #print(request.POST["description"])
    return HttpResponseRedirect(reverse("index"))
