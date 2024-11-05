from fastapi import APIRouter, FastAPI, Request, Response


health_router = APIRouter()


@health_router.get("/health")
def health_check(request: Request) -> dict:
    return {"status": "ok"}
