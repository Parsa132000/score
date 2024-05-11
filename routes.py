from fastapi import APIRouter, Depends
from .service import SaveRating, GetUserRatings, GetAverageRating

router = APIRouter(tags=['ratings'], prefix='/ratings')

@router.post("/save")
def save_rating(save_rating_request: SaveRating):
    return save_rating_request()

@router.get("/user/{user_id}")
def get_user_ratings(user_id: str):
    return GetUserRatings(user_id)()

@router.get("/average")
def get_average_rating():
    return GetAverageRating()()