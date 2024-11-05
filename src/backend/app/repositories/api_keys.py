from utils import Generator
from storage import Database


class APIKeyRepository:
    @staticmethod
    async def create() -> dict:
        async with Database() as client:
            return await client.apikey.create({"key": Generator.generate_api_key()})

    @staticmethod
    async def find_by_key(key: str) -> dict:
        async with Database() as client:
            api_key = await client.apikey.find_unique(where={"key": key})
            return api_key

    @staticmethod
    async def find_all() -> list:
        async with Database() as client:
            api_keys = await client.apikey.find_many()
            return api_keys

    @staticmethod
    async def delete(key: str) -> dict:
        async with Database() as client:
            api_key = await client.apikey.delete(where={"key": key})
            return api_key

    @staticmethod
    async def delete_all() -> dict:
        async with Database() as client:
            api_keys = await client.apikey.delete_many()
            return api_keys
