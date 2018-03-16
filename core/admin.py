from django.contrib import admin
from .models import ToDo, Task

class ToDoAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'modified']
	list_search = ['name', 'slug']
	list_filter = ['created', 'modified']


class TaskAdmin(admin.ModelAdmin):
	list_display = ['name', 'done', 'deadline', 'todo', 'created', 'modified']
	list_search = ['name', 'done', 'deadline', 'todo',]
	list_filter = ['created', 'modified', 'done', 'deadline']

# Register your models here.
admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Task, TaskAdmin)
