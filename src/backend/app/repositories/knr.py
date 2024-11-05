from storage import Database
from typing import Optional
import pandas as pd
from prisma import Json, enums


class KNRRepository:
    @staticmethod
    async def create(
        id: str,
        data: dict,
        prediction: enums.PredictResult = enums.PredictResult.NOT_PROCESSED,
    ) -> dict:
        async with Database() as client:
            knr = await client.knr.create(
                data={"id": id, "data": Json(data), "prediction": prediction}
            )
            return knr

    @staticmethod
    async def find_by_id(id: str) -> Optional[dict]:
        async with Database() as client:
            knr = await client.knr.find_unique(where={"id": id})
            return knr

    @staticmethod
    async def find_all(where: Optional[dict] = None) -> list[dict]:
        async with Database() as client:
            knrs = await client.knr.find_many(where=where)
            return knrs

    @staticmethod
    async def update(
        id: str, data: Optional[dict] = None, prediction: Optional[str] = None
    ) -> dict:
        async with Database() as client:
            update_data = {}
            if data is not None:
                update_data["data"] = data
            if prediction is not None:
                update_data["prediction"] = prediction
            knr = await client.knr.update(where={"id": id}, data=update_data)
            return knr

    @staticmethod
    async def delete(id: str) -> dict:
        async with Database() as client:
            knr = await client.knr.delete(where={"id": id})
            return knr

    @staticmethod
    async def delete_all() -> dict:
        async with Database() as client:
            result = await client.knr.delete_many()
            return result
