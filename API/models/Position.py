from django.db import models

from base_model.models import AbstractModel


class Position(AbstractModel):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
