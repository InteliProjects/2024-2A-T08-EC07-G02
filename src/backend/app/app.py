from fastapi import FastAPI


class AppWrapper:
    __app: FastAPI = None

    def __init__(self) -> FastAPI:
        self.__app = FastAPI()

    def get_app(self) -> FastAPI:
        return self.__app
