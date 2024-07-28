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

            data = response.json()

            # Check if the response contains rows and elements
            if not data.get("rows"):
                raise Exception("No rows found in the Google Maps API response")

            elements = data["rows"][0].get("elements")
            if not elements:
                raise Exception("No elements found in the Google Maps API response")

            # Check the status of the element
            element_status = elements[0].get("status")
            if element_status != "OK":
                raise Exception(f"Google Maps API returned status: {element_status}")

            distance = elements[0]["distance"]["value"]
            return distance

        except requests.Timeout as e:
            raise Exception("The request to the Google Maps API timed out") from e
        except requests.RequestException as e:
            raise Exception(
                f"An error occurred while requesting the Google Maps API: {str(e)}"
            ) from e
        except KeyError as e:
            raise Exception(
                f"Unexpected response format from Google Maps API: {str(e)}"
            ) from e
