from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('admin/', views.admin, name='main'),
    path('user/', views.user, name='user'),
    path('edit/', views.edit, name='edit'),
    path('dashboard/', views.dashboard_user, name='dashboard_user'),
    path('', views.login, name='login')
]