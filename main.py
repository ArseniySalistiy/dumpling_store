from fastapi import FastAPI
from app.routers import routes

app = FastAPI()

app.include_router(routes.router) #здесь запускается приложение тк apirouter не поддерживает uvicorn сервер