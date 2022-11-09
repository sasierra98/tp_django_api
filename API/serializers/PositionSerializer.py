from rest_framework import serializers

from API.models.Position import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')
