from contextlib import asynccontextmanager

import uvicorn
from api import auth
from core.config.settings import settings
from db import redis_db
from db.postgres import create_database
from fastapi import FastAPI
from redis.asyncio import Redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.entity import User  # noqa: F401
    await create_database()
    redis_db.redis = Redis(host=settings.redis.redis_host, port=settings.redis.redis_port)

    yield

    await redis_db.redis.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.project.project_name,
    docs_url=settings.project.docs_url,
    openapi_url=settings.project.openapi_url,
    version=settings.project.version,
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # noqa: S104
        port=8000,
    )
