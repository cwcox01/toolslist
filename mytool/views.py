from django.shortcuts import render
from django.http import HttpResponse
from .models import Tool, Battery

# Create your views here.


def index(request):
    return render(request, 'mytools.html')


def home(request):
    return render(request, 'home.html')


def display_tools(request):
    tools = Tool.objects.all()
    return render(request, 'mytools.html', {'tools': tools})
