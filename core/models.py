from django.db import models
from django.urls import reverse

# Create your models here.
class ToDo (models.Model):
	
	name = models.CharField('List', max_length=200)
	slug = models.SlugField('Id', max_length=200, unique=True)
	done = models.BooleanField('Done')

	created = models.DateTimeField('Crieted', auto_now_add=True)
	modified = models.DateTimeField('Modified', auto_now=True)

	class Meta:
		verbose_name='To do'
		verbose_name_plural='To do\'s'
		ordering=['modified']

	def __str__(self):
		return self.name

class Task (models.Model):

	name = models.CharField('Task', max_length=200)
	slug = models.SlugField('Id', max_length=200, unique=True)
	done = models.BooleanField('Done', default=False, blank=True)
	todo = models.ForeignKey('core.ToDo', on_delete=models.CASCADE, verbose_name='To do')
	deadline = models.DateTimeField('Deadline')

	created = models.DateTimeField('Created', auto_now_add=True)
	modified = models.DateTimeField('Modified', auto_now=True)

	class Meta:
		verbose_name='Task'
		verbose_name_plural='Tasks'
		ordering=['modified']

	def __str__ (self):
		return self.name