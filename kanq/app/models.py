from django.db import models

COLOR_CHOICES = [
    ('light-red','Rojo'),
    ('light-green','Verde'),
    ('light-blue', 'Azul'),
]

# Create your models here.
class task(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    #color = models.CharField(max_length=11, choices=COLOR_CHOICES, default='light-red')

    def __str__(self):
        return self.task
