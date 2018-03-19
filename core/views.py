from django.shortcuts import render

from .models import ToDo, Task
# Create your views here.
def index (request):
	context = {
		'todos' : ToDo.objects.all(),
		'tasks' : Task.objects.all(),
	}
	return render(request, 'index.html', context)