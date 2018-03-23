from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo, Task
from .forms import TodoForm, TaskForm
# Create your views here.
def index (request):
	todo_form = TodoForm(request.POST or None)
	if todo_form.is_valid() and not Todo.objects.filter(slug=todo_form.cleaned_data['slug']):
		Todo.objects.create(name=todo_form.cleaned_data['name'], slug=todo_form.cleaned_data['slug'], done=todo_form.cleaned_data['done'])

	# task_form = TaskForm(request.POST or None)
	# if task_form.is_valid() and not Task.objects.filter(slug=task_form.cleaned_data['slug']):
	# 	Task.objects.create(name=task_form.cleaned_data['name'], slug=task_form.cleaned_data['slug'],
	# 		todo=task_form.cleaned_data['todo'], done=task_form.cleaned_data['done'], 
	# 		deadline = task_form.cleaned_data['deadline'])

	context = {
		'todos' : Todo.objects.all(),
		'tasks' : Task.objects.all(),
		'todo_form'	: todo_form,
		#'task_form' : task_form,
	}
	return render(request, 'index.html', context)

def todo_delete (request, slug):
	todo = Todo.objects.get(slug=slug)
	todo.delete()
	return HttpResponseRedirect('/')

def task_delete (request, slug):
	task = Task.objects.get(slug=slug)
	task.delete()
	return HttpResponseRedirect('/')

def todo_update (request, slug):
	pass
