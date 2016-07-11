from django.db import models

# Create your models here.
class University(models.Model):
	name = models.CharField(max_len = 100)
	points = models.PositiveIntergerField()
	password = models.CharField(max_len = 25)

