from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import DESCENDING
from .model import Rating

class RatingMongoDB:
    def __init__(self, db_url: str, db_name: str, collection_name: str):
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    async def save_rating(self, rating: Rating):
        await self.collection.insert_one(rating.dict())

    async def get_user_ratings(self, user_id: str):
        ratings = await self.collection.find({'user_id': user_id}).sort('timestamp', DESCENDING).to_list(None)
        return [Rating(**rating) for rating in ratings]

    async def get_average_rating(self):
        pipeline = [
            {"$group": {"_id": None, "average_rating": {"$avg": "$rating"}}}
        ]
        result = await self.collection.aggregate(pipeline).to_list(length=1)
        return result[0]["average_rating"] if result else None

ratings_db = RatingMongoDB(db_url="mongodb://localhost:27017", db_name="mydatabase", collection_name="Ratings")