from fastapi import FastAPI
from app.api.routes import router as api_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)

