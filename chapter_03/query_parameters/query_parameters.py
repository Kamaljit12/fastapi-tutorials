from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel


app = FastAPI(name="Query Parameters")

@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}


class UserFormat(str, Enum):
    SHORT: str = "short"
    LONG: str = "long"

@app.get("/users_format")
async def get_users_format(format: UserFormat):
    return {"format": format}

@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


@app.get("/user_query")
async def get_user_query(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)