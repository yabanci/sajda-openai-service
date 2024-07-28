from models.trip_request import TripRequest
from services.google_maps import GoogleMapsService
from services.openai_service import OpenAIService


class TripPlanner:
    def __init__(self):
        self.google_maps_service = GoogleMapsService()
        self.openai_service = OpenAIService()

    async def plan_trip(self, request: TripRequest):
        if not request.days_in_mecca:
            request.days_in_mecca = round(0.7 * request.days)
        if not request.days_in_medina:
            request.days_in_medina = round(0.3 * request.days)

        itinerary = self.plan_itinerary(
            request.days, request.days_in_mecca, request.days_in_medina
        )
        hotels_in_mecca = await self.find_hotels(
            "Mecca", request.max_distance_to_mosque
        )
        try:
            hotels_in_medina = await self.find_hotels(
                "Medina", request.max_distance_to_mosque
            )
        except Exception as e:
            return {f"Error finding hotels in Medina: {e}"}
        flights = await self.find_flights(
            request.city_of_departure,
            itinerary["arrival_city"],
            itinerary["departure_city"],
            request.interval,
        )

        return {
            "itinerary": itinerary,
            "hotels_in_mecca": hotels_in_mecca,
            "hotels_in_medina": hotels_in_medina,
            "flights": flights,
        }

    def plan_itinerary(self, total_days, days_in_mecca, days_in_medina):
        return {
            "total_days": total_days,
            "days_in_mecca": days_in_mecca,
            "days_in_medina": days_in_medina,
            "arrival_city": "Jeddah",
            "departure_city": "Medina",
        }

    async def find_hotels(self, city, max_distance_to_mosque):
        hotels = await self.openai_service.get_hotels(city, max_distance_to_mosque)
        filtered_hotels = []
        for hotel in hotels:
            try:
                distance = self.google_maps_service.get_distance_to_mosque(hotel, city)
                if distance <= max_distance_to_mosque:
                    hotel["distance_to_mosque"] = distance
                    filtered_hotels.append(
                        {
                            "name": hotel["name"],
                            "city": hotel["city"],
                            "link": hotel["link"],
                            "distance_to_mosque": distance,
                        }
                    )
            except Exception as e:
                print(f"Error getting distance for hotel {hotel['name']}: {e}")

        return filtered_hotels

    async def find_flights(self, departure_city, arrival_city, return_city, interval):
        return await self.openai_service.get_flights(
            departure_city, arrival_city, return_city, interval
        )
