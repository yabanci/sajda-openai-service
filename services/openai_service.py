import json

import openai

from config.settings import OPENAI_API_KEY


class OpenAIService:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-3.5-turbo"

    async def get_hotels(self, city, max_distance_to_mosque):
        openai_response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"List hotels in {city} within {max_distance_to_mosque} meters of the central mosque. (in json format: name, city, link)",
                }
            ],
        )
        hotels = json.loads(openai_response.choices[0].message.content)
        return hotels

    async def get_flights(self, departure_city, arrival_city, return_city, interval):
        openai_response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Find flights from {departure_city} to {arrival_city} and returning from {return_city} within the interval {interval}. (in json format: aviacompany, price in kzt, link)",
                }
            ],
        )
        flights = json.loads(openai_response.choices[0].message.content)
        return flights
