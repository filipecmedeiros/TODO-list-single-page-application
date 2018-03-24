"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
	path('', views.index, name='index'),
	path(r'todo_delete/<slug>/', views.todo_delete, name='todo_delete'),
    path(r'todo_update/<slug>/', views.TodoUpdateView.as_view(), name='todo_update'),
    path(r'task_delete/<slug>/', views.task_delete, name='task_delete'),
    path(r'task_update/<slug>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('admin/', admin.site.urls),
]
