from django.db import models
import uuid
# Create your models here.

class Task(models.Model):
    # id = models.AutoField(editable = False, primary_key=True, unique=True)
    priority_choices = (('1', 'High'),('2', 'Normal'),('3', 'Low'))
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True,editable = False)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=priority_choices, default=priority_choices[1])

    def __str__(self):
        return self.description
