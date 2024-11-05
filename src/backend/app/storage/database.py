from prisma import Prisma
from fastapi import Depends


class Database:
    def __init__(self) -> None:
        self.__prisma = Prisma()

    async def __aenter__(self) -> Prisma:
        await self.__prisma.connect()
        return self.__prisma

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.__prisma.disconnect()

    @property
    def prisma(self) -> Prisma:
        return self.__prisma
