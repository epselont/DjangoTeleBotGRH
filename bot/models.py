from django.db import models

# Create your models here.

class Button(models.Model):
	button = models.CharField(max_length=200)

	def __str__(self):
		return self.button