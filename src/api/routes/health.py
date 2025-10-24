from fastapi import APIRouter

health = APIRouter(tags=["health"])


@health.get("/health")
def healthcheck():
    return {"status": "ok"}
