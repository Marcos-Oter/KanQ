from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import task

# Register your models here.

@admin.register(task)
class StoresAdmin(ModelAdmin):
    ...