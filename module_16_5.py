from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def new_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "messages": users})


@app.get("/user/{user_id}")
def all_users(request: Request, user_id) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "messages": user_id})


@app.post("/user/{username}/{age}")
def created_users(username: str, age: str):
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return users


@app.put("/user/{user_id}/{username}/{age}")
def update_users(user_id: str, username: str, age: str) -> str:
    try:
        if user_id in users:
            user_id = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
        raise HTTPException(status_code=404, detail="User was not found")
