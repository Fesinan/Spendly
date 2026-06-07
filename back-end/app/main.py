import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from .database import Base, engine
from .routes.transactions import router as transactions_router

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Spendly API", version="0.1.0", lifespan=lifespan)

app.include_router(transactions_router)


@app.get("/api/health")
def health():
    return {"status": "ok"}
