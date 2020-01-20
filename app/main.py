from fastapi import FastAPI

from app.core import config
from app.middleware.db import DBConnection
from app.api.v1.api import api_router

app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

app.add_middleware(DBConnection)
app.include_router(api_router)