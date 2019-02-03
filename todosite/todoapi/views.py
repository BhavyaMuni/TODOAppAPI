from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets
from django.shortcuts import render
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    # for i in Task.objects.all():
    #     if i.is_completed == False:
    #         queryset = queryset + i
    queryset = Task.objects.filter(is_completed = False)
    serializer_class = TaskSerializer

class DonetaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(is_completed = True)
    serializer_class = TaskSerializer

class AlltasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def WebpageView(request):
    objects = Task.objects.filter(is_completed = False)
    sorted_objects = sorted(objects, key=lambda x: x.priority)
    objects_done = Task.objects.filter(is_completed =True)
    return render(request, template_name='index.html',context={'tasks_undone': sorted_objects, 'tasks_done':objects_done})