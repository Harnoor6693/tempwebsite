from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Startegies', views.startegies, name='startegies'),
    path('Goals', views.goals, name='goals'),
    path('Position', views.position, name='position'),
    path('Role', views.role, name='role'),
    path('References', views.references, name='references'),
]