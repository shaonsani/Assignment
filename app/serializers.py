from rest_framework import serializers
from app.models import GlucoseReading


class GlucoseReadingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseReading
        fields = ("reading_uuid", "patient_uuid", "value", "unit", "recorded_at",)