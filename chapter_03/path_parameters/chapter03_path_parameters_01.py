from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
import uvicorn

# create app for fastapi
app = FastAPI()


# hello world
@app.get("/")
async def hello():
    return {"message": "Hello World"}


# get user by id
@app.get("/users/{id}")
async def get_user(id: int):
    return {"id": id}

# get user by type
class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

# get user by type
@app.get("/users/type/{user_type}")
async def get_users(user_type: UserType):
    return {"user_type": user_type}


# create user
class User(BaseModel):
    name: str
    user_type: UserType

# create user
@app.post("/users/}")
async def create_user(user: User):
    return {"user": user}


# Schema for request JSON
class ChatRequest(BaseModel):
    message: str   # user query will be in "message"

# Schema for response JSON
class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Access the JSON value using request.message
    user_input = request.message
    reply = f"You said: {user_input}"
    return ChatResponse(response=reply)



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=True)