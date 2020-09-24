from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('timezone', views.timezone),
]
app_name = 'home'