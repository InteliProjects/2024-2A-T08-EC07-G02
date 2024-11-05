import pandas as pd
import logging
import io
import os
from fastapi import UploadFile

logger = logging.getLogger(__name__)


async def read_file_param(file: UploadFile) -> pd.DataFrame:
    content = await file.read()
    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension == ".csv":
        df = pd.read_csv(io.BytesIO(content))
        logger.debug(f"CSV file '{file.filename}' read into DataFrame.")
    elif file_extension == ".parquet":
        df = pd.read_parquet(io.BytesIO(content))
        logger.debug(f"Parquet file '{file.filename}' read into DataFrame.")
    elif file_extension == ".xlsx":
        df = pd.read_excel(io.BytesIO(content))
        logger.debug(f"Excel file '{file.filename}' read into DataFrame.")
    else:
        error_msg = "Unsupported file type. Only CSV and Parquet are supported."
        logger.error(error_msg)
        raise ValueError(error_msg)

    return df
