from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.template import loader
from . models import task
import random

colors = [
    'light-red',
    'light-green',
    'light-blue',
]
#from django.views.generic import TemplateView

# Create your views here.

#class home(TemplateView):
#    template_name="main-index.html"

def index (request):
    return render(request, "app/main-index.html")

def crud(request):
    #template = loader.get_template("app/index.html")
    db_data = task.objects.all()

    '''random_colors = [random.choice(colors) for obt in range(0, len(db_data))]
    cards_list = [[random_colors[index], task_obj] for index, task_obj in enumerate(db_data)]
    print(cards_list)'''

    context = {
        "db_data": db_data[::-1],
        "update": None
    }
    print(db_data)
    #return HttpResponse(template.render(context, request))


    return render(request, "app/index.html", context)


def create(request):
    try:
        task_task = request.POST["task"]
        task_description = request.POST["description"]
        #Si el los campos de texto están vacíos no crea creará la tarea en base de datos.
        if not task_task or not task_description:
            raise ValueError("El texto no puede quedar vacío.")

        db_data = task(task=task_task, description=task_description)
        db_data.save()
        #print(request.POST["task"])
        #print(request.POST["description"])
        return HttpResponseRedirect(reverse("crud"))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("crud"))
    
def update(request):
    task_id = request.POST["id"]
    task_task = request.POST["task"]
    task_description = request.POST["description"]
    db_data = task.objects.get(pk=task_id)
    db_data.task = task_task
    db_data.description = task_description
    db_data.save()
    return HttpResponseRedirect(reverse("crud"))
    
def update_form(request, task_id):
    #template = loader.get_template("app/index.html")
    db_data = task.objects.all()
    db_data_only= task.objects.get(pk=task_id)

    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    print(db_data)
    #return HttpResponse(template.render(context, request))
    return render(request, "app/index.html", context)

def delete(request, task_id):

    db_data = task.objects.filter(id=task_id)
    db_data.delete()

    return HttpResponseRedirect(reverse("crud"))
