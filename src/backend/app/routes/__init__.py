from .api_keys import keys_router
from .health_check import health_router
from .knr import knr_router
from .datalake import datalake_router
from .model import model_router
from .charts_router import charts_router
from fastapi import FastAPI, APIRouter


def setup(app: FastAPI):
    api_router = APIRouter(prefix="/api")

    api_router.include_router(health_router)
    api_router.include_router(keys_router)
    api_router.include_router(knr_router)
    api_router.include_router(datalake_router)
    api_router.include_router(model_router)
    api_router.include_router(charts_router)

    app.include_router(api_router)
