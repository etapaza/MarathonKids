from django.db import models

class Counter:
    count = 0

    def next(self):
        self.count += 1
        return self.count


# Create your models here.
class University(models.Model):
	name = models.CharField(max_length=100)
	points = models.PositiveIntegerField()
	password = models.CharField(max_length=25)

