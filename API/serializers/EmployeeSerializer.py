from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError

from API.models import Employee


class ConsultantSerializer(serializers.ModelSerializer):
    position_name = fields.SerializerMethodField(required=False)

    @staticmethod
    def get_position_name(consultant: Employee):
        return getattr(consultant.position, 'name', None)

    def validate(self, attrs):
        data = super(ConsultantSerializer, self).validate(attrs)
        if not data['position'].id == 1:
            raise ValidationError({'position': "Position is not allowed"})
        return data

    def save(self, **kwargs):
        print(**kwargs)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'position', 'position_name', 'identification', 'city', 'sex', 'age')

