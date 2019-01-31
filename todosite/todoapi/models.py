from django.db import models
import uuid
# Create your models here.

class Task(models.Model):
    # id = models.AutoField(editable = False, primary_key=True, unique=True)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True,editable = False)
    is_completed = models.BooleanField(default=False)

