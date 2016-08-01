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
	money_raised = models.PositiveIntegerField(default=0)
	kids_enrolled = models.PositiveIntegerField(default=0)
	social_media = models.PositiveIntegerField(default=0)
