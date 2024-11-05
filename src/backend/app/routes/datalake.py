from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import os
import io
import logging
from services import DatalakeService
from typing import Optional
from utils import read_file_param

datalake_router = APIRouter(prefix="/datalake")

logger = logging.getLogger(__name__)


@datalake_router.post("/")
async def insert(file: UploadFile = File(...)):
    try:
        df = await read_file_param(file)

        table_name = os.path.splitext(file.filename)[0]
        logger.debug(f"Using table name '{table_name}' for insertion.")

        DatalakeService.create_table(df, table_name)
        logger.info(f"Table '{table_name}' created successfully in the datalake.")

        df_info = {
            "filename": file.filename,
            "rows": df.shape[0],
            "columns": df.shape[1],
        }
        return df_info

    except Exception as e:
        logger.exception("An error occurred while inserting data into the datalake.")
        raise HTTPException(status_code=500, detail=str(e))


@datalake_router.get("/")
async def get_list():
    try:
        tables_df = DatalakeService.list_tables()
        table_names: List[str] = tables_df["name"].tolist()
        logger.debug("Retrieved list of tables from the datalake.")
        return {"tables": table_names}

    except Exception as e:
        logger.exception("An error occurred while retrieving the list of tables.")
        raise HTTPException(status_code=500, detail=str(e))


@datalake_router.get("/{table_name}")
async def get_table(
    table_name: str, page: int = 0, per_page: int = 10, knr_query: Optional[str] = None
):
    if page < 0 or per_page < 1:
        error_msg = (
            "Invalid pagination parameters. Page must be >= 0 and per_page must be > 0."
        )
        logger.error(error_msg)
        raise HTTPException(status_code=400, detail=error_msg)

    try:
        table_df, total_count = DatalakeService.get_table_paginator(
            table_name,
            page=page,
            per_page=per_page,
            knr_query=knr_query,
        )
        logger.debug(f"Retrieved table '{table_name}' from the datalake.")

        table_slice = table_df.to_dict(orient="records")

        return {"data": table_slice, "total_count": total_count}

    except Exception as e:
        logger.exception(f"An error occurred while retrieving table '{table_name}'.")
        raise HTTPException(status_code=500, detail=str(e))


@datalake_router.delete("/{table_name}")
async def delete_table(table_name: str):
    try:
        DatalakeService.delete_table(table_name)
        logger.info(f"Table '{table_name}' deleted successfully from the datalake.")
        return JSONResponse(status_code=204, content={"message": "Table deleted."})

    except Exception as e:
        logger.exception(f"An error occurred while deleting table '{table_name}'.")
        raise HTTPException(status_code=500, detail=str(e))
