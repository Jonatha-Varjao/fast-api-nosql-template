from app.db.mongodb import db
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class DBConnection(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.db = db.client
        response = await call_next(request)
        request.state.db.close()
        return response

def get_db(request: Request):
    return request.state.db
