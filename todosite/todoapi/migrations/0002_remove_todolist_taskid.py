# Generated by Django 2.1.4 on 2019-01-29 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='taskid',
        ),
    ]
