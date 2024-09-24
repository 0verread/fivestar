from typing import Dict

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas.user import UserRegister
from schemas.auth import Token
import crud.user as user_crud
from database.database import get_db

router = APIRouter()

@router.post("/login", response_model=Token)
def login_with_pass(form_data: OAuth2PasswordRequestForm = Depends(), 
					db: Session = Depends(get_db)) -> Dict[str, any]:
	access_token = user_crud.login(email=form_data.username, password=form_data.password, db=db)
	return {"access_token": access_token, "token_type": "brearer"}

@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister, db: Session = Depends(get_db)) -> Dict[str, any]:
	user_in_db = user_crud.get_user_by_email(email=user.email, db=db)
	if user_in_db:
		raise HTTPException(status_code=status.HTTP_409_CONFLICT,
							detail="The user with this {user.email} already exists",)
	new_user = user_crud.create(user=user, db=db)
	return {"message": "User created", "user": new_user}

@router.post("/token", response_model=Token)
def get_refresh_token(user: UserRegister, db: Session = Depends(get_db)) -> Dict[str, any]:
	user_in_db = user_crud.get_user_by_email(email=user.email)
	return ""
