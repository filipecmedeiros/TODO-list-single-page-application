from django import forms

from .models import Todo, Task

class TodoForm (forms.ModelForm):
	class Meta:
		model= Todo
		fields = '__all__'

class TaskForm (forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'