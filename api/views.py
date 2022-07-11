from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(["GET"])
def api_overview(request):
    api_urls = {"list": "/task-list"}
    return Response(api_urls)
