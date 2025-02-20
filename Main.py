from typing import List
from fastapi import FastAPI
from Services import Read

App = FastAPI()

@App.get("/root", response_model=List[dict])
async def ReadRoot():
    return Read.Register()