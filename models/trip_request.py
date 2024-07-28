from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date
import re

class TripRequest(BaseModel):
    days: int
    interval: str
    city_of_departure: str
    days_in_mecca: int = None
    days_in_medina: int = None
    max_distance_to_mosque: int = 500

    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator('interval')
    def parse_interval(cls, v):
        pattern = re.compile(r"(\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})")
        match = pattern.match(v)
        if not match:
            raise ValueError("Interval must be in the format 'YYYY-MM-DD to YYYY-MM-DD'")
        start_date_str, end_date_str = match.groups()
        cls.start_date = date.fromisoformat(start_date_str)
        cls.end_date = date.fromisoformat(end_date_str)
        return v
