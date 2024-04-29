from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Visit

class VisitCreateSerializer(serializers.ModelSerializer):

    def validate_schedule(self, value):
        visit_count = value.visits.count()
        print(visit_count)
        if 3 <= visit_count:
            raise ValidationError("Превышено максимальрое количество мест")
        return value

    class Meta:
        model = Visit
        fields = ['patient', 'service', 'schedule']