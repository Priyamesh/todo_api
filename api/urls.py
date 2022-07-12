from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.api_overview, name="overview"),
    path("/task-list", views.taskList, name="taskList"),
    path("/task-list/<int:pk>", views.taskDetail, name="task"),
    path("/task-create", views.taskCreate, name="task-create"),
    path("/task-update/<int:pk>", views.taskUpdate, name="task-update"),
    path("/task-delete/<int:pk>", views.taskDelete, name="task-delete"),
]
