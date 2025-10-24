from fastapi import FastAPI
from .routes.parse import parse
from .routes.health import health


app = FastAPI(title="Recruitment AI Platform", version="0.1.0")

app.include_router(health)
app.include_router(parse)
