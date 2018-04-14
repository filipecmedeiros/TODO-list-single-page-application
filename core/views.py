from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views import generic

from .models import Todo, Task
from .forms import TodoForm, TaskForm
# Create your views here.
def index (request):
	context = {
		'todos' : Todo.objects.prefetch_related('task_set'),
		'todo_form'	: TodoForm(),
		'task_form' : TaskForm(),
	}
	return render(request, 'index.html', context)

class TodoCreateView (generic.CreateView):
	model = Todo
	form_class = TodoForm
	success_url = reverse_lazy ('index')

class TaskCreateView (generic.CreateView):
	model = Task
	form_class = TaskForm
	success_url = reverse_lazy ('index')


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