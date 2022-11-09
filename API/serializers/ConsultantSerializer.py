from rest_framework import serializers

from API.models import Consultant


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('id', 'name', 'position', 'identification', 'city', 'sex', 'age')
