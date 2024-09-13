from fastapi import APIRouter, HTTPExeption, status

router = APIRouter()

@router.post("/login", response_model=Token)
def login_with_pass():
	pass