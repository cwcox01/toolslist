from django.urls import path

from . import views

urlpatterns = [
    path('mytools/', views.index, name='index'),
    path('', views.home, name="home")
]
