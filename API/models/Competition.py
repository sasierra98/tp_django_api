from django.db import models

from base_model.models import AbstractModel
from API.models import Employee


class Competition(AbstractModel):
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
