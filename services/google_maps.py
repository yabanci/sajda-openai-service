import requests
from config.settings import GOOGLE_MAPS_API_KEY

class GoogleMapsService:
    def get_distance_to_mosque(self, hotel_address, city):
        mosque_address = 'Masjid al-Haram, Mecca' if city.lower() == 'mecca' else 'Al-Masjid an-Nabawi, Medina'
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={hotel_address}&destinations={mosque_address}&key={GOOGLE_MAPS_API_KEY}"
        response = requests.get(url)
        distance = response.json()['rows'][0]['elements'][0]['distance']['value']
        return distance
