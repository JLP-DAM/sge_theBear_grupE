from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

import os

from typing import List

from services import user
from models.User import User

app = FastAPI()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_database():
    database = Session(engine)

    try:
        yield database
    finally:
        database.close()

@app.get("/users/", response_model=List[dict])
async def read_user(database:Session = Depends(get_database)):
    result = user.get_all_users(database)
    return result

@app.post("/users/", response_model=dict)
async def create_user(name: str, email: str, database:Session = Depends(get_database)):
    user.create_user(name, email, database)

    return {"message": "Created user successfully"}

@app.put("/users/", response_model=dict)
async def update_user(id: int, name: str, email: str, database:Session = Depends(get_database)):
    return user.update_user(id, name, email, database)

@app.delete("/users/", response_model=dict)
async def update_user(id: int, database:Session = Depends(get_database)):
    return user.delete_user(id, database)