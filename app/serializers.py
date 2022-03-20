from rest_framework import serializers
from app.models import GlucoseReading


class GlucoseReadingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseReading
        fields = ("reading_uuid", "patient_uuid", "value", "unit", "recorded_at",)


class GlucoseReadingUpdateSerializer(GlucoseReadingBaseSerializer):
    class Meta(GlucoseReadingBaseSerializer.Meta):
        extra_kwargs = ({
            "patient_uuid": {
                "required": False
            },
            "unit": {
                "required": False
            },
            "value": {
                "required": False
            },
            "recorded_at": {
                "required": False
            }})
            