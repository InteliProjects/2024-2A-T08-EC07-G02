from services import ModelService, KNRService
from fastapi import APIRouter, FastAPI, Request, Response, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
import time
import os
import boto3
from utils import read_file_param
from pipelines import ModelPipeline
from typing import List

model_router = APIRouter(prefix="/model")


@model_router.post("/train")
async def request(
    failures: UploadFile = File(...),
    results: UploadFile = File(...),
    status: UploadFile = File(...),
    tags: List[str] = [],
):
    try:
        failures_df = await read_file_param(failures)
        results_df = await read_file_param(results)
        status_df = await read_file_param(status)

        pipeline = ModelPipeline(failures_df, results_df, status_df)

        model_filename = f"model_{time.strftime('%Y%m%d%H%M%S')}.joblib"
        local_model_path = os.path.join("/tmp", model_filename)

        pipeline.run(local_model_path)

        s3_model_path = f"models/{model_filename}"
        print(f"Uploading model to S3: {s3_model_path} with tags: {tags}")
        ModelService.upload_model(local_model_path, tags)
        ModelService.update_model_path(s3_model_path, tags)

        if os.path.exists(local_model_path):
            os.remove(local_model_path)

        return {"status": "success", "model_path": f"s3://{S3_BUCKET}/{s3_model_path}"}

    except Exception as e:
        return {"status": "error", "message": str(e)}


@model_router.get("/")
async def list_models():
    models = ModelService.get_models()
    return {"models": models}


@model_router.get("/download/{model_id}")
async def download_model(model_id: str):
    try:
        model_path = ModelService.get_model(model_id)

        filename = os.path.basename(model_path)

        s3_model_path = ModelService.get_model(model_id)

        return {
            "status": "success",
            "message": f"Model '{model_id}' successfully retrieved.",
            "url": s3_model_path,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@model_router.delete("/{model_id}")
async def delete_model(model_id: str):
    try:
        ModelService.delete_model(model_id)
        return {
            "status": "success",
            "message": f"Model '{model_id}' successfully deleted.",
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@model_router.post("/select/{model_id}")
async def select_model(model_id: str):
    try:
        ModelService.update_model_path(model_id)
        return {
            "status": "success",
            "message": f"Model '{model_id}' successfully selected.",
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@model_router.get("/selected")
async def selected_model():
    model = ModelService.get_model_path()
    if model is None:
        return {"model": None}
    return {"model": model.split("/")[-1]}
