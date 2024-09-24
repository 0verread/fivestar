from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from database.database import get_db
from models.users import User
from utils.auth import get_password_hash, create_access_token
from utils.uids import UniqueIds
from schemas.user import UserRegister

def login(email: str, password: str, db: Session) -> str:
	invalid_cred_err_msg = "Invalid Email or password"
	try:
		db_user = get_user_by_email(email=email, db=db) 
		is_validated = db_user.verify_password(password)
		if is_validated is not True:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=invalid_cred_err_msg)
	except:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=invalid_cred_err_msg)
	access_token = create_access_token(data={"sub": email})
	return access_token
	

def get_user_by_email(email: str, db: Session):
	# TODO: should be cached
	user = db.query(User).filter(User.email == email).first()
	print(user)
	return user

def create(user: UserRegister, db: Session):
	db_user = db.query(User).filter(User.email == user.email).first()
	if db_user:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already registered")
	hashed_password = get_password_hash(user.password)
	new_user_id = UniqueIds("usr_").get_id()
	new_user = User(id=new_user_id, email=user.email, hashed_password=hashed_password)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user

