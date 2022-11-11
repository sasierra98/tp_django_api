from django.db import models

from API.models import Position, CategoryCompetition
from base_model.models import AbstractModel


class Participant(AbstractModel):
    participant_name = models.CharField(max_length=50)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)
    identification = models.BigIntegerField()
    city = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    category_competition = models.ForeignKey(to=CategoryCompetition, on_delete=models.CASCADE)
