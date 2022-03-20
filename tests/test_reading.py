import json
import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestReadingCreateListAPI:
    end_point = "/v1/reading"

    def test_create_success(self, api_client, payload):
        response = api_client.post(path=self.end_point, data=payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("patient_uuid") == payload.get("patient_uuid")

    def test_create_fail_with_invalid_uuid(self, api_client, payload):
        payload["patient_uuid"] = "22c685ae-9249-4c84-9b6e-"
        response = api_client.post(path=self.end_point, data=payload, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_reading_list(self, api_client, payload):
        api_client.post(path=self.end_point, data=payload, format='json')
        api_client.post(path=self.end_point, data=payload, format='json')
        response = api_client.get(path=self.end_point, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 2
        