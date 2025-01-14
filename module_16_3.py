from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
def create_user(username: Annotated[
    str, Path(min_length=1, max_length=30, description="Enter your username", example="UrbanUser")],
                age: Annotated[int, Path(ge=18, le=100, description="Enter your age", example=24)]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20
    , description="Enter username", example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120
    , description="Enter age", example=24)]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    del users[user_id]
    return f'Users with {user_id} deleted'

