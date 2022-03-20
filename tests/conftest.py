import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def payload():
    data = {
        "patient_uuid": "22c685ae-9249-4c84-9b6e-d0e3537be66e",
        "value": 5.5,
        "unit": "mmol/L",
        "recorded_at": "2021-01-01T09:15:00+00:00"
    }
    return data