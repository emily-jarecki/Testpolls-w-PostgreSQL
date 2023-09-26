from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    car = models.CharField(max_length=80)
    def __str__(self):
        return self.name

