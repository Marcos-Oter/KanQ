from django.db import models

# Create your models here.
class task(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.task
