# Generated by Django 5.0 on 2023-12-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(default='light-red', max_length=12),
        ),
    ]
