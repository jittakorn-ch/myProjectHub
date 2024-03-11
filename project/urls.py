from django.urls import path

from . import views

app_name = 'project'
urlpatterns = [
    path('', views.project, name='project'),
    path('todolist/', views.todolist, name='todolist'),
    path('todolist/add', views.todolistAdd, name='todolistAdd'),
]