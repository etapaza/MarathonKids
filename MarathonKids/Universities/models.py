from django.db import models
from django.contrib.auth.models import AbstractUser

class Counter:
    count = 0

    def next(self):
        self.count += 1
        return self.count

# Create your models here.
class University(AbstractUser):
	name = models.CharField(max_length=100)
	points = models.PositiveIntegerField()
	kids_enrolled = models.PositiveIntegerField(default=0)
	miles_ran = models.PositiveIntegerField(default=0)
