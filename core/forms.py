from django import forms

from .models import Todo

class TodoForm (forms.Form):
	name = forms.CharField (label="Title")
	slug = forms.SlugField (label="Id")
	done = forms.BooleanField (label="Done", required=False)

class TaskForm (forms.Form):
	name = forms.CharField (label='Title')
	slug = forms.SlugField (label='Id')
	todo = forms.ModelChoiceField (label='List', queryset=Todo.objects.all())
	deadline = forms.DateTimeField(label='Deadline')
	done = forms.BooleanField(label='Done', required=False)
	