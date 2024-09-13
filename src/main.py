from fastapi import FastAPI

app = FastAPI(title="Fivestar API", version="0.1.0")

@app.get("/")
def root():
	return {"message": "Fivestar API running successfully"}