from fastapi import FastAPI
from enum import Enum


app = FastAPI()

@app.get("/")
async def hello_world():
    return {"Hello": "World"}
