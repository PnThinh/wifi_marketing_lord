from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('admin/', views.admin, name='main'),
    path('admin/user/', views.admin_user, name='admin_user'),
    path('edit/', views.edit, name='edit'),
    path('dashboard/', views.dashboard_user, name='dashboard_user'),
    path('user/', views.user, name='user'),
    path('user/location/', views.user_location, name='user_location'),
    path('user/customer/', views.user_customer, name='user_customer'),
    path('', views.login, name='login')
]