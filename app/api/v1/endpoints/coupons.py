from typing import List, Optional

from bson import ObjectId
from fastapi import APIRouter, Depends, Query

from app.db.mongodb import AsyncIOMotorClient
from app.middleware.db import get_db
from app.schema.coupon import CouponBase, CouponInDB

router = APIRouter()

@router.get('/')
async def get_coupons(
    db: AsyncIOMotorClient = Depends(get_db),
    limit: int = Query(10, gt=0),
    skip: int = Query(0, ge=0),
) -> List[CouponInDB] :
    coupons: List[CouponInDB] = []
    rows = db['<database>']['<collection>'].find(limit=limit, skip=skip)
    coupons = [ CouponInDB(**row) async for row in rows ]
    return coupons

@router.get('/{id}')
async def get_coupon(
    db: AsyncIOMotorClient = Depends(get_db),
    *,
    id: str
) -> CouponInDB :
    coupon = db['<database>']['<collection>'].find_one({"_id":ObjectId(id) })
    return CouponInDB(**coupon)
    

@router.post('/{id}')
async def create_coupon(
    db: AsyncIOMotorClient = Depends(get_db),
    *,
    coupon_data: CouponBase
) -> CouponInDB :
    coupon = coupon_data.dict()
    await db['<database>']['<collection>'].insert_one(coupon)
    coupon['_id']
    return CouponInDB( **coupon )


@router.delete('/{id}')
async def delete_coupon(
    db: AsyncIOMotorClient = Depends(get_db),
    *,
    id: str
) -> CouponBase :
    await db['<database>']['<collection>'].delete_one({"_id": ObjectId(id)})
    
