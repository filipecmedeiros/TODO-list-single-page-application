from django import forms

class ToDoForm (forms.Form):
	name = forms.CharField (label="Title")
	slug = forms.SlugField (label="Id")
	done = forms.BooleanField (label="Done", required=False)

