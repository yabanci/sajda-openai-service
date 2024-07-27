import openai
from config.settings import OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    async def get_hotels(self, city, max_distance_to_mosque):
        openai_response = openai.chat.completions.create(
            model="text-davinci-003",
            prompt=f"List hotels in {city} within {max_distance_to_mosque} meters of the central mosque.",
            max_tokens=100
        )
        hotels = openai_response.choices[0].text.strip().split("\n")
        return [{'name': hotel, 'address': f'{hotel}, {city}'} for hotel in hotels]

    async def get_flights(self, departure_city, arrival_city, return_city, interval):
        openai_response = openai.chat.completions.create(
            model="text-davinci-003",
            prompt=f"Find flights from {departure_city} to {arrival_city} and returning from {return_city} within the interval {interval}.",
            max_tokens=100
        )
        flights = openai_response.choices[0].text.strip().split("\n")
        return flights
