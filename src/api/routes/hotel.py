from typing import Dict

from sqlalchemy.orm import Session

from fastapi.security import Depends
from fastapi import APIRouter

from database.database import get_db
from schemas.hotel import CreateHotelSchema

router  = APIRouter()

@router.post("/hotel", response_model=Dict[str, any])
def create_hotel(hotel = CreateHotelSchema, db: Session = Depends(get_db)):
	pass

@router.get("/hotel", response_model=Dict[str, any])
def get_hotel_detail():
	pass

