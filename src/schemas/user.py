from pydantic import BaseModel, ConfigDict, EmailStr 

from typing import Optional

class UserBase(BaseModel):
	email: Optional[EmailStr] = None
	is_active: bool = True
	full_name: Optional[str] = None

class UserRegister(BaseModel):
	email: EmailStr
	password: str 
	full_name: Optional[str] = None

