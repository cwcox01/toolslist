from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mytool import views

urlpatterns = [
    path('', include('mytool.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile')
]
