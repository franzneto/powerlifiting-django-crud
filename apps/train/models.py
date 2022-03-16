from __future__ import annotations
from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Train(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    repetitions = models.IntegerField()
    weight = models.IntegerField()
    tonnage = models.IntegerField(blank=True, null=True, default=None)

    def calc_tonnage(self):
        self.tonnage = self.weight * self.repetitions

    def set_user(self, user):
        self.user = user

    def __str__(self):
        return f"{self.exercise} - {self.weight} - {self.date.strftime('%d/%m/%Y')}"
