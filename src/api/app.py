from fastapi import FastAPI
from fastapi import APIRouter
from .routes.parse import router as parse_router

app = FastAPI(title="Recruitment AI Platform", version="0.1.0")

health = APIRouter(tags=["health"])


@health.get("/health")
def healthcheck():
    return {"status": "ok"}


app.include_router(health)
app.include_router(parse_router)
