import pytest

from services.openai_service import OpenAIService


@pytest.mark.asyncio
async def test_get_hotels(monkeypatch):
    async def mock_create(*args, **kwargs):
        class MockResponse:
            choices = [
                {"text": '[{"name": "Hotel Mecca", "address": "Mecca, Address"}]'}
            ]

        return MockResponse()

    monkeypatch.setattr("openai.Completion.create", mock_create)

    openai_service = OpenAIService()
    response = await openai_service.get_hotels("Mecca", 500)

    assert response == '[{"name": "Hotel Mecca", "address": "Mecca, Address"}]'


@pytest.mark.asyncio
async def test_get_flights(monkeypatch):
    async def mock_create(*args, **kwargs):
        class MockResponse:
            choices = [{"text": '[{"flight": "NYC to Jeddah"}]'}]

        return MockResponse()

    monkeypatch.setattr("openai.Completion.create", mock_create)

    openai_service = OpenAIService()
    response = await openai_service.get_flights(
        "NYC", "Jeddah", "Medina", "2024-08-01 to 2024-08-10"
    )

    assert response == '[{"flight": "NYC to Jeddah"}]'
