from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retrieve_chickens,
    add_chicken,
)
from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    ChickenSchema,
)

router = APIRouter()

@router.post("/", response_description="Chicken data added into the database")
async def add_chicken_data(chicken: ChickenSchema = Body(...)):
    chicken = jsonable_encoder(chicken)
    new_chicken = await add_chicken(chicken)
    return ResponseModel(new_chicken, "Chicken added successfully.")