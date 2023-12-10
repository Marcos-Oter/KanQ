from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("",views.index, name="index"),
    path("crud/",views.crud, name="crud"),
    path("create/", views.create, name="create"),
    path("update", views.update, name="update"),
    path("update/<int:task_id>", views.update_form, name="update_form"),
    path("delete/<int:task_id>", views.delete, name="delete"),
    path('admin/', admin.site.urls,name="admin"), 
]
