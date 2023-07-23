from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_projects, name = 'projects'),
    path('add-projects', views.add_projects, name='add-projects'),
]