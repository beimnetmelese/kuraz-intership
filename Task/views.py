from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.completed = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
