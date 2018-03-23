from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDo, Task
from .forms import ToDoForm
# Create your views here.
def index (request):
	
	context = {
		'todos' : ToDo.objects.all(),
		'tasks' : Task.objects.all(),
		'ToDoForm'	: ToDoForm(),
	}
	return render(request, 'index.html', context)

def ToDoDelete (request, slug):
	todo = ToDo.objects.get(slug=slug)
	todo.delete()
	return HttpResponseRedirect('/')
