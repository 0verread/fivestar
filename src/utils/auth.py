import jwt
import bcrypt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from utils.secrets import Secrets

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verfify_password(plain_password: str, hashed_password: str):
	return bcrypt.checkpw(plain_password, hashed_password)

def get_password_hash(plain_password: str):
	return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf8')

def create_access_token(data: dict):
	to_encode = data.copy()
	expire = datetime.utcnow() + timedelta(minutes=Secrets.ACCESS_TOKEN_EXPIRE_MINS)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, Secrets.SECRET_KEY, algorithm=Secrets.ALGORITHM)
	return encoded_jwt


def verify_token(token: str):
	try:
		payload = jwt.decode(token, Secrets.SECRET_KEY, algorithm=[Secrets.ALGORITHM])
		username:  str = payload.get("sub")
		if username is None:
			return None
		return username
	except jwt.PyJWTError:
		return None
