from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDo, Task
from .forms import ToDoForm, TaskForm
# Create your views here.
def index (request):
	todo_form = ToDoForm(request.POST or None)
	if todo_form.is_valid() and not ToDo.objects.filter(slug=todo_form.cleaned_data['slug']):
		ToDo.objects.create(name=todo_form.cleaned_data['name'], slug=todo_form.cleaned_data['slug'], done=todo_form.cleaned_data['done'])

	task_form = TaskForm(request.POST or None)
	if task_form.is_valid() and not Task.objects.filter(slug=task_form.cleaned_data['slug']):
		Task.objects.create(name=task_form.cleaned_data['name'], slug=task_form.cleaned_data['slug'],
			todo=task_form.cleaned_data['todo'], done=task_form.cleaned_data['done'], 
			deadline = task_form.cleaned_data['deadline'])

	context = {
		'todos' : ToDo.objects.all(),
		'tasks' : Task.objects.all(),
		'todo_form'	: todo_form,
		'task_form' : task_form,
	}
	return render(request, 'index.html', context)

def ToDoDelete (request, slug):
	todo = ToDo.objects.get(slug=slug)
	todo.delete()
	return HttpResponseRedirect('/')

def TaskDelete (request, slug):
	task = Task.objects.get(slug=slug)
	task.delete()
	return HttpResponseRedirect('/')
