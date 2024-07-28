import requests

from config.settings import GOOGLE_MAPS_API_KEY


class GoogleMapsService:
    def get_distance_to_mosque(self, hotel_address, city, timeout=10):
        mosque_address = (
            "Masjid al-Haram, Mecca"
            if city.lower() == "mecca"
            else "Al-Masjid an-Nabawi, Medina"
        )
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={hotel_address}&destinations={mosque_address}&key={GOOGLE_MAPS_API_KEY}"
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code
            distance = response.json()["rows"][0]["elements"][0]["distance"]["value"]
            return distance
        except requests.Timeout as e:
            raise Exception("The request to the Google Maps API timed out") from e
        except requests.RequestException as e:
            raise Exception(
                f"An error occurred while requesting the Google Maps API: {str(e)}"
            ) from e
