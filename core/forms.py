from django import forms

from .models import ToDo

class ToDoForm (forms.Form):
	name = forms.CharField (label="Title")
	slug = forms.SlugField (label="Id")
	done = forms.BooleanField (label="Done", required=False)

class TaskForm (forms.Form):
	name = forms.CharField (label='Title')
	slug = forms.SlugField (label='Id')
	todo = forms.ModelChoiceField (label='List', queryset=ToDo.objects.all())
	deadline = forms.DateTimeField(label='Deadline')
	done = forms.BooleanField(label='Done', required=False)
	