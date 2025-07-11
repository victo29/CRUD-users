from fastapi import FastAPI

from src.main.routes import user_routes

app = FastAPI()
app.include_router(user_routes.router)
