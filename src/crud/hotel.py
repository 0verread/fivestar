from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from database.database import get_db
from utils.uids import UniqueIds
from schemas.hotel import CreateHotelSchema
from bcrypt 


def create_new_hotel(hotel: CreateHotelSchema, db: Session):
	pass

def update_hotel_details(hotel: UpdateHotelSchema, db: Session):
	pass 

def get_hotel_details(hotel: UpdateHotelSchema, db: Session):
	pass 
