from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://172.17.0.4:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, username='root', password='example')

database = client.chickens

chickens_collection = database.get_collection("chickens_collection")


def chicken_helper(chicken) -> dict:
    return {
        "id": str(chicken["_id"]),
        "name": str(chicken["name"]),
    }


# Retrieve all students present in the database
async def retrieve_chickens():
    chickens = []
    async for chicken in chickens_collection.find():
        chickens.append(chicken_helper(chicken))
    return chickens

# Add a new student into to the database
async def add_chicken(chicken_data: dict) -> dict:
    chicken = await chickens_collection.insert_one(chicken_data)
    new_chicken = await chickens_collection.find_one({"id": chicken.inserted_id})
    return chicken_helper(new_chicken)
