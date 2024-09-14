from fastapi import APIRouter, HTTPException, status
from schemas.auth import Token
from schemas.user import UserRegister


router = APIRouter()

@router.post("/login", response_model=Token)
def login_with_pass():
	pass

@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister):
	user = user_crud.get_user_by_email(email=user.email)
	if user:
		raise HTTPException(status_code=status.HTTP_409_CONFLICT,
							detail=f"The user with this {user.email} already exists")

	if user.password is None:
		raise HTTPException(status_code=status.HTTP_409_CONFLICT,
							detail=f"Can not create user. password is needed")

	user_crud.create(user)
	return {"messasge": "User created succeesfully"}

