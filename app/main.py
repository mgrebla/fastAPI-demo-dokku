from fastapi import FastAPI

from app.server.routes import router as ChickenRouter

app = FastAPI()

app.include_router(ChickenRouter, tags=["Chicken"], prefix="/chicken")

@app.get("/")
async def root():
    return {"message": "Hello World"}
