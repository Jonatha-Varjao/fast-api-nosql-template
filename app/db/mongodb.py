from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URI

class DataBase:
    client: AsyncIOMotorClient = None

db = DataBase()
db.client = AsyncIOMotorClient(MONGODB_URI)
db.client['1help']['users'].create_index( [("name", 1)], unique=True )
db.client['1help']['discounts'].create_index( [("name", 1)], unique=True )