from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

users =[]

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
def all_users() -> List[User]:
    return users

@app.post(path="/user/{username}/{age}")
def created_users(user: User):
    if not user.id:
        user.id = len(all_users()) + 1
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, user: User):
    try:
        user.id = user_id
        return users
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    try:
        users.pop(user_id)
        return users
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")