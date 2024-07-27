from pydantic import BaseModel

class TripRequest(BaseModel):
    days: int
    interval: str
    city_of_departure: str
    days_in_mecca: int = None
    days_in_medina: int = None
    max_distance_to_mosque: int = 500
