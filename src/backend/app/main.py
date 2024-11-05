import uvicorn
from fastapi import FastAPI
from app import AppWrapper
from fastapi.middleware.cors import CORSMiddleware
from routes import setup as setup_routes
import logging
import dotenv

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)

app_wrapper = AppWrapper()
app = app_wrapper.get_app()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"],
)

setup_routes(app)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Starting server on http://0.0.0.0:3333")
    uvicorn.run(app, host="0.0.0.0", port=3333)
