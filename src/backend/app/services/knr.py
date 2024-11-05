from repositories import KNRRepository
from prisma import enums
from pipelines import ModelPipeline
import pandas as pd


class KNRService:
    @staticmethod
    async def get_knrs() -> dict:
        knrs = await KNRRepository.find_all()
        return knrs

    @staticmethod
    async def create_knr(
        id: str,
        data: dict,
        prediction: enums.PredictResult = enums.PredictResult.NOT_PROCESSED,
    ) -> dict:
        results_df = pd.DataFrame(data["results"])
        status_df = pd.DataFrame(data["status"])
        pipeline = ModelPipeline(None, results_df, status_df)
        result = pipeline.run(None)
        knr = await KNRRepository.create(id=id, data=data, prediction=prediction)
        return dict(knr)

    @staticmethod
    async def get_knr(id: str) -> dict:
        knr = await KNRRepository.find_by_id(id=id)
        return dict(knr) if knr else None

    @staticmethod
    async def set_prediction(id: str, prediction: str) -> dict:
        knr = await KNRRepository.update(id=id, prediction=prediction)
        return dict(knr)

    @staticmethod
    async def delete_knr(id: str) -> dict:
        knr = await KNRRepository.delete(id=id)
        return dict(knr)

    @staticmethod
    async def delete_all_knrs() -> dict:
        result = await KNRRepository.delete_all()
        return result

    @staticmethod
    async def get_last_knr_processed() -> dict:
        knrs = await KNRRepository.find_all(
            {"prediction": {"not": enums.PredictResult.NOT_PROCESSED}}
        )
        if knrs:
            return dict(knrs[-1])
        return None
