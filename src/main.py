from fastapi import FastAPI

from api import auth_router

app = FastAPI(title="Fivestar API", version="0.1.0")


app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
	return {"message": "Fivestar API running successfully"}