
from fastapi import FastAPI
from .routes import router as ratings_router
from .repository import ratings_db

app = FastAPI()

app.include_router(ratings_router)

@app.on_event("startup")
async def startup_db_client():
    await ratings_db.client.startup()

@app.on_event("shutdown")
async def shutdown_db_client():
    await ratings_db.client.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)