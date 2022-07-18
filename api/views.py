from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Task


# Create your views here.


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "/task-list": "list",
        "/task-list/<int:pk>": "task-detail",
        "/task-create": "task create",
        "/task-update/<int:pk>": "task update",
        "/task-delete/<int:pk>": "task delete",
    }
    return Response(api_urls)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all().order_by("-id")
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def taskCreate(request):
    # print(request.POST, "hello")
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["GET"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item deleted Sucessful")
