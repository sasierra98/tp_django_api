from django.db import models

from base_model.models import AbstractModel


class CategoryCompetition(AbstractModel):
    name = models.CharField(max_length=20)