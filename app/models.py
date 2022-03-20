import uuid
from django.db import models


class GlucoseReading(models.Model):
    UNIT_1 = "mmol/L"
    UNIT_2 = "mg/dL"
    UNIT_CHOICES = [
        (UNIT_1, "mmol/L"),
        (UNIT_1, "mg/dL")
    ]
    reading_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    patient_uuid = models.UUIDField()
    value = models.FloatField()
    unit = models.CharField(choices=UNIT_CHOICES, max_length=10)
    recorded_at = models.DateTimeField()

    def __str__(self):
        return f"{self.reading_uuid} | {self.recorded_at}"