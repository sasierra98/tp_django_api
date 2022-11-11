from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError

from API.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    position_name = fields.SerializerMethodField(required=False)

    @staticmethod
    def get_position_name(competition: Participant):
        return getattr(competition.position, 'name', None)

    def validate(self, attrs):
        data = super(ParticipantSerializer, self).validate(attrs)
        if not data['position'].id == 1:
            raise ValidationError({'position': "Position is not allowed"})
        return data

    def save(self, **kwargs):
        print(**kwargs)

    class Meta:
        model = Participant
        fields = ('id', 'name', 'position', 'position_name', 'identification', 'city', 'sex', 'age')

