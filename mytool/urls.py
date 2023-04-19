from django.urls import path

from . import views

urlpatterns = [
    path('mytools/', views.display_tools, name='index'),
    path('', views.home, name="home")
]
