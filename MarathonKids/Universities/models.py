from django.db import models

# Create your models here.
class University(models.Model):
	name = models.CharField(max_length=100)
	points = models.PositiveIntegerField()
	password = models.CharField(max_length=25)

