from fastapi import APIRouter

from app.api.v1.endpoints import user, service, coupons

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(service.router, prefix="/services", tags=["Services"])
api_router.include_router(coupons.router, prefix="/coupons", tags=["Coupons"])