from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from app.db.mongodb import AsyncIOMotorClient
from app.middleware.db import get_db
from app.schema.user import UserInDB, UserBase
from bson import ObjectId

router = APIRouter()

@router.get('/', response_model=List[ Optional[UserInDB] ] )
async def get_users(
    db: AsyncIOMotorClient = Depends(get_db),
    limit: int = Query(10, gt=0),
    skip: int = Query(0, ge=0),
) -> List[ Optional[UserInDB] ] :
    
    users: List[UserInDB] = []

    rows = db['<database>']['<collection>'].find(limit=limit, skip=skip)
    users = [ UserInDB(**row) async for row in rows ]
    
    return users

@router.post('/', response_model=UserInDB )
async def create_user(
    db: AsyncIOMotorClient = Depends(get_db),
    *,
    user: UserBase
) -> UserInDB :
    user_doc = user.dict()
    await db['<database>']['<collection>'].insert_one(user_doc)
    user_doc['_id']
    return UserInDB( **user_doc )


@router.delete('/{id}' )
async def delete_user(
    db: AsyncIOMotorClient = Depends(get_db),
    *,
    id: str
):
    await db['<database>']['<collection>'].delete_one({"_id": ObjectId(id)})
