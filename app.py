from fastapi import FastAPI
from database import db

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "MongoDB connected 🚀"}

@app.post("/users")
async def create_user():
    user = {"name": "John"}
    await db.users.insert_one(user)
    return {"status": "inserted"}

@app.get("/users")
async def get_users():
    users = []
    async for user in db.users.find():
        user["_id"] = str(user["_id"])  # convert ObjectId
        users.append(user)
    return users