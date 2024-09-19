import os
from dotenv import load_dotenv

load_dotenv()

class Secrets:
	DATABASE_URL = os.getenv("DATABASE_URL")
	SECRET_KEY = os.getenv("SECRET_KEY")
	ALGORITHM = os.getenv("ALGORITHM")
	ACCESS_TOKEN_EXPIRE_MINS = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINS"))
	