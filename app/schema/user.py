from typing import List, Optional

from app.schema.base import DBModelMixin
from app.schema.rwmodel import RWModel

class UserBase(RWModel):
    name: str
    coupons: Optional[List[str]] = []

class UserInDB(DBModelMixin, UserBase):
    pass