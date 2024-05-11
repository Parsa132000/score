from .model import Rating
from .repository import ratings_db

class SaveRating:
    def __init__(self, user_id: str, rating: int):
        self.user_id = user_id
        self.rating = rating

    def __call__(self):
        rating = Rating(user_id=self.user_id, rating=self.rating)
        ratings_db.save_rating(rating)
        return {"message": "Rating saved successfully."}

class GetUserRatings:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def __call__(self):
        ratings = ratings_db.get_user_ratings(self.user_id)
        return ratings

class GetAverageRating:
    def __call__(self):
        average_rating = ratings_db.get_average_rating()
        return average_rating