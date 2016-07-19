from django.db import models

class Counter:
    count = 0

    def next(self):
        self.count += 1
        return self.count

# Create your models here.
class University(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=25)
	domain = models.CharField(max_length=500, default="ncaa.org")
	points = models.PositiveIntegerField()
	kids_enrolled = models.PositiveIntegerField(default=0)
	miles_ran = models.PositiveIntegerField(default=0)
	

