from typing import List
from fastapi import FastAPI
from services import read
from sqlmodel import Session, select, create_engine

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

@app.put("/items/")
async def update_users():
    with Session(engine) as session:
        result = read.registre()
        statement = select(result).where(result.name == "Roger")
        results = session.exec(statement)
        user = results.one()
        print("User:", user)

        user.age = 16
        session.add(user)
        session.commit()
        session.refresh(user)
        print("Updated user:", user)