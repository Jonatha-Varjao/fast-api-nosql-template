"""
"name": "TIRTOP",
"type": "ABSOLUTE",
"value": 20
"""

from typing import List, Optional

from datetime import datetime
from pydantic import Field, root_validator

from app.schema.base import DBModelMixin, ObjectIdStr
from app.schema.rwmodel import RWModel

class CouponBase(RWModel):
    name: str
    type: str
    value: int

class CouponInDB(DBModelMixin, CouponBase):
    pass