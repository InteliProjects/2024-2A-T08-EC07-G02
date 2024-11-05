from repositories import APIKeyRepository
from prisma import Prisma
from storage import Database


class APIKeyService:
    @staticmethod
    async def get_keys() -> dict:
        return await APIKeyRepository.find_all()

    @staticmethod
    async def create_key() -> dict:
        repository = APIKeyRepository(db)
        return dict(await APIKeyRepository.create())
