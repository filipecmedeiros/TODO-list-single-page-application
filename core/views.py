from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import generic

from .models import Todo, Task
from .forms import TodoForm, TaskForm
# Create your views here.
def index (request):
	todo_form = TodoForm(request.POST or None)
	if todo_form.is_valid() and not Todo.objects.filter(slug=todo_form.cleaned_data['ident']):
		Todo.objects.create(name=todo_form.cleaned_data['title'], 
			slug=todo_form.cleaned_data['ident'], done=todo_form.cleaned_data['completed']
		)

	task_form = TaskForm(request.POST or None)
	if task_form.is_valid() and not Task.objects.filter(slug=task_form.cleaned_data['slug']):
		Task.objects.create(name=task_form.cleaned_data['name'], slug=task_form.cleaned_data['slug'],
			todo=task_form.cleaned_data['todo'], done=task_form.cleaned_data['done'], 
			deadline = task_form.cleaned_data['deadline']
			)

	context = {
		'todos' : Todo.objects.all(),
		'tasks' : Task.objects.all(),
		'todo_form'	: todo_form,
		'task_form' : task_form,
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

class TodoUpdateView (generic.UpdateView):

	model = Todo
	template_name = 'todo_update.html'
	fields = ['name', 'slug', 'done']
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(TodoUpdateView, self).get_context_data(**kwargs)
		context['Todo'] = get_object_or_404(Todo, slug=self.kwargs['slug'])
		return context

class TaskUpdateView (generic.UpdateView):

	model = Task
	template_name = 'task_update.html'
	fields = ['name', 'slug', 'todo', 'deadline', 'done']
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(TaskUpdateView, self).get_context_data(**kwargs)
		context['Task'] = get_object_or_404(Task, slug=self.kwargs['slug'])
		return context