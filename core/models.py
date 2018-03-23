from django.db import models
from django.urls import reverse

# Create your models here.
class ToDo (models.Model):
	
	name = models.CharField('Nome', max_length=200)
	slug = models.SlugField('Identificador', max_length=200, unique=True)
	done = models.BooleanField('Feito')

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name='A fazer'
		verbose_name_plural='A fazeres'
		ordering=['modified']

	def __str__(self):
		return self.name

class Task (models.Model):

	name = models.CharField('Tarefa', max_length=200)
	done = models.BooleanField('Feito', default=False)
	todo = models.ForeignKey('core.ToDo', on_delete=models.CASCADE, verbose_name='A fazer')
	deadline = models.DateTimeField('Data limite')

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name='Tarefa'
		verbose_name_plural='Tarefas'
		ordering=['modified']

	def __str__ (self):
		return self.name