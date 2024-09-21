from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from database.database import get_db
from models.users import User
from utils.auth import get_password_hash
from utils.uids import UniqueIds
from schemas.user import UserRegister

def login(email, password, db: Session):
	
	pass

def get_user_by_email(email, db: Session):
	user = db.query(User).filter(User.email == email).first()
	return user

def create(user: UserRegister, db: Session):
	db_user = db.query(User).filter(User.email == user.email).first()
	if db_user:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already registered")
	hashed_password = get_password_hash(user.password)
	new_user_id = UniqueIds("usr-").get_id()
	new_user = User(id=new_user_id, email=user.email, hashed_password=hashed_password)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user

