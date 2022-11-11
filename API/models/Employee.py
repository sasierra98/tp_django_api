from django.db import models

from API.models import Position
from base_model.models import AbstractModel


class Employee(AbstractModel):
    name = models.CharField(max_length=150)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)
    identification = models.BigIntegerField()
    city = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
