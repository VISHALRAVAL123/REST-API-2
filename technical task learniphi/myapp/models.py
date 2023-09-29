from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
	number=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	description=models.TextField()
	date=models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title