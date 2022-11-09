from django.db import models

from cities_light.models import SubRegion
from API.models import Position
from base_model.models import AbstractModel

SEX_CHOICES = (
    ('male', 'male'),
    ('female', 'female')
)


class Consultant(AbstractModel):
    name = models.CharField(max_length=150)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)
    identification = models.BigIntegerField(unique=True)
    city = models.CharField(max_length=30)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10)
    age = models.PositiveSmallIntegerField()
