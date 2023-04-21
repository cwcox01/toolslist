from django.urls import path

from . import views

urlpatterns = [
    path('tool/', views.display_tools, name='tools'),
    path('', views.home, name="home"),
    path('battery', views.display_batteries, name="battery")
]
