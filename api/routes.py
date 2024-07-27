from fastapi import APIRouter, HTTPException

from core.trip_planner import TripPlanner
from models.trip_request import TripRequest

router = APIRouter()


@router.post("/trip")
async def plan_trip(request: TripRequest):
    try:
        trip_planner = TripPlanner()
        response = await trip_planner.plan_trip(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
