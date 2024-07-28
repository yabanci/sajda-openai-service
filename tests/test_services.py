import pytest
import requests

from services.google_maps import GoogleMapsService
from services.openai_service import OpenAIService


# Mock the settings for the tests
class MockSecrets:
    GOOGLE_MAPS_API_KEY = "mock_google_maps_api_key"
    OPENAI_API_KEY = "mock_openai_api_key"


# Mock Google Maps Service Test
def test_google_maps_service(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {"rows": [{"elements": [{"distance": {"value": 1000}}]}]}

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    google_maps_service = GoogleMapsService()
    distance = google_maps_service.get_distance_to_mosque("mock_address", "Mecca")
    assert distance == 1000


# Mock OpenAI Service Test
@pytest.mark.asyncio
async def test_openai_service_get_hotels(monkeypatch):
    async def mock_create(*args, **kwargs):
        class MockResponse:
            choices = [{"text": "Hotel Mecca\nHotel Medina"}]

        return MockResponse()

    monkeypatch.setattr("openai.Completion.create", mock_create)

    openai_service = OpenAIService()
    hotels = await openai_service.get_hotels("Mecca", 500)
    assert hotels == [
        {"name": "Hotel Mecca", "address": "Hotel Mecca, Mecca"},
        {"name": "Hotel Medina", "address": "Hotel Medina, Mecca"},
    ]


@pytest.mark.asyncio
async def test_openai_service_get_flights(monkeypatch):
    async def mock_create(*args, **kwargs):
        class MockResponse:
            choices = [{"text": "Flight NYC to Jeddah\nFlight Jeddah to NYC"}]

        return MockResponse()

    monkeypatch.setattr("openai.Completion.create", mock_create)

    openai_service = OpenAIService()
    flights = await openai_service.get_flights(
        "NYC", "Jeddah", "Medina", "2024-08-01 to 2024-08-10"
    )
    assert flights == ["Flight NYC to Jeddah", "Flight Jeddah to NYC"]
