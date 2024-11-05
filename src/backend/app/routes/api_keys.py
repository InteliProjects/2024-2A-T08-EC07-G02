from fastapi import APIRouter, Depends
from services.api_keys import APIKeyService
from prisma import Prisma

keys_router = APIRouter(prefix="/keys")


@keys_router.get("/")
async def get_data() -> dict:
    return {"keys": await APIKeyService.get_keys()}


@keys_router.post("/")
async def create_key() -> dict:
    return await APIKeyService.create_key()
