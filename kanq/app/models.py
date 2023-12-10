from django.db import models

color_choices = (
    ('light-red', 'Rojo'),
    ('light-green', 'Verde'),
    ('light-blue', 'Azul'),
    ('light-yellow', 'Amarillo'),
)

# Create your models here.
class task(models.Model):
    name = models.CharField(max_length=30, default=' ')
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=20, choices=color_choices, default='light-red')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.task
