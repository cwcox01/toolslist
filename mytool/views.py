from django.shortcuts import render
from django.http import HttpResponse
from .models import Tool, Battery
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.


def tools(request):
    return render(request, 'tool.html')


def home(request):
    return render(request, 'home.html')


def battery(request):
    return render(request, 'batteries.html')


def display_tools(request):
    tools = Tool.objects.all()
    return render(request, 'tool.html', {'tools': tools})


def display_batteries(request):
    battery = Battery.objects.all()
    return render(request, 'batteries.html', {'battery': battery})


def my_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'my_template.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
