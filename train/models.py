from __future__ import annotations
from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Train(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    annotation = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    repetitions = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.exercise} - {self.date}"



