from typing import List
from fastapi import FastAPI
from Services import Read

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def ReadRoot():
    return Read.Register()