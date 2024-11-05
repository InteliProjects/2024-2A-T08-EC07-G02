from services import ModelService, KNRService
from fastapi import APIRouter, FastAPI, Request, Response
from pydantic import BaseModel
import time
from prisma import enums
import prisma

knr_router = APIRouter(prefix="/knr")


class KNR(BaseModel):
    knr: str
    data: dict


@knr_router.get("/predict/{knr}")
async def predict(knr: str):
    knr_record = await KNRService.get_knr(knr)
    if knr_record:
        start_time = time.perf_counter()
        prediction = ModelService.predict(knr_record["data"])
        end_time = time.perf_counter()

        await KNRService.set_prediction(
            knr,
            enums.PredictResult.FAILURE if prediction else enums.PredictResult.NORMAL,
        )

        process_time = end_time - start_time
        return {
            "prediction": {
                "result": prediction,
                "process_time_ms": round(process_time * 1000, 2),
            }
        }


@knr_router.get("/")
async def list_knrs():
    return {"knrs": await KNRService.get_knrs()}


@knr_router.post("/")
async def new_knr(knr: KNR):
    try:
        new_knr = await KNRService.create_knr(knr.knr, knr.data)
    except prisma.errors.UniqueViolationError:
        return {"knr": {"error": "KNR_ALREADY_EXISTS"}}

    return {"knr": new_knr}


@knr_router.get("/{knr}")
async def get_knr(knr: str):
    knr = await KNRService.get_knr(knr)
    if knr:
        return {"knr": knr}
    return {"knr": {"error": "NOT_FOUND"}}


@knr_router.get("/last/processed")
async def get_last_knr():
    knr = await KNRService.get_last_knr_processed()
    if knr:
        return {"knr": knr}
    return {"knr": {"error": "NOT_FOUND"}}
