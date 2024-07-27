import requests
from fastapi.testclient import TestClient

from api.main import app
from services.google_maps import GoogleMapsService

client = TestClient(app)


def test_plan_trip():
    response = client.post(
        "/trip",
        json={
            "days": 10,
            "interval": "2024-08-01 to 2024-08-10",
            "city_of_departure": "Almaty",
            "max_distance_to_mosque": 500,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "itinerary" in data
    assert "hotels_in_mecca" in data
    assert "hotels_in_medina" in data
    assert "flights" in data


def test_google_maps_timeout(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.Timeout("Mock timeout")

    monkeypatch.setattr(requests, "get", mock_get)

    google_maps_service = GoogleMapsService()
    try:
        google_maps_service.get_distance_to_mosque("mock_address", "Mecca")
    except Exception as e:
        assert str(e) == "The request to the Google Maps API timed out"
