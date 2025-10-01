from fastapi import FastAPI, Path
from enum import Enum
import uvicorn


app = FastAPI()


# path parameters 01
# @app.get("/users/{id}")
# async def get_user(id: int):
#     return {"id": id}


# path parameters 02
# @app.get("/users/{type}/{id}")
# async def get_user(type: str, id: int):
#     return {"type": type, "id": id}


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


# path parameters 3

# @app.get("/users/{type}/{id}")
# async def get_user(type: UserType, id: int):
#     return {"type": type, "id": id}

# path parameters 4

# • gt: Greater than
# • ge: Greater than or equal to
# • lt: Less than
# • le: Less than or equal to


# @app.get("/users/{id}")
# async def get_user(id: int = Path(..., ge=5000, le=5999)):
#     return {"id": id}

# path_parameters_05

# @app.get("/licence-plates/{license}")
# async def get_license_plates(license: str = Path(..., min_length=9, max_length=9)):
#     return {"license": license}

# path_parameters_06

# gegx format

# Starts with 2 word characters (\w{2}): letters, digits, or underscore
# Followed by 3 digits (\d{3})
# Then a hyphen (-)
# Ends with 2 word characters (\w{2})

@app.get("/license-plates/{license}")
async def get_license(license: str = Path(..., regex=r"^\w{2}\d{3}-\w{2}$")):
    return {"license": license}



