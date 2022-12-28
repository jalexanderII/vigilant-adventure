# https://www.youtube.com/watch?v=nZhAW-JQ8NM&t=167
from collections import defaultdict
from datetime import datetime
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json

from models.tasks.tasks import Task

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks_for_user = defaultdict(list)
mock_users = {
    "joella@gmail.com": "1234",
    "armando@gmail.com": "1234",
    "jerod@gmail.com": "1234",
    "joel@gmail.com": "1234",
}


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

# define endpoint
@app.get("/")
def Home():
    return "Welcome home"


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    try:
        while True:
            data = await websocket.receive_text()
            message = {"time": current_time, "client": client_id, "message": data}
            await manager.broadcast(json.dumps(message))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = {"time": current_time, "client_id": client_id, "message": "Offline"}
        await manager.broadcast(json.dumps(message))


@app.post("/create_task/{content}/{username}/{priority}")
def create_task(content: str, username: str, priority: str):
    new_task = Task(
        content=content,
        completed=False,
        username=username,
        created_at=datetime.now(),
        completed_at=None,
        priority=priority,
        task_id=len(tasks_for_user[username]) + 1,
    )
    tasks_for_user[username].append(new_task)
    return tasks_for_user


@app.post("/set_task_completed/{username}/{task_id}")
def set_task_completed(username: str, task_id: int):
    if username in tasks_for_user:
        tasks_list = tasks_for_user.get(username)
        for task in tasks_list:
            if task.task_id == task_id:
                task.completed = True
                task.completed_at = datetime.now()
                return task
        return "task doesn't exist"
    return "user doesn't exist"


@app.get("/login/{user}/{password}")
def login(user: str, password: str):
    if user in mock_users:
        db_password = mock_users.get(user)
        if db_password == password:
            return "True"
        else:
            return "Wrong Password"
    else:
        return "User not found"


@app.post("/signup/{user}/{password}")
def signup(user: str, password: str):
    if user in mock_users:
        return "User already exists"
    else:
        mock_users[user] = password
        return "User created"


@app.get("/tasks/{username}")
def get_tasks(username: str):
    if username in tasks_for_user:
        return tasks_for_user.get(username)


@app.delete("/task/{username}/{task_id}")
def task_delete(task_id: int, username: str):
    if username in tasks_for_user:
        tasks_list = tasks_for_user.get(username)
        for task in tasks_list:
            if task.task_id == task_id:
                tasks_list.remove(task)
            return task
        return "task doesn't exist"
    return "user doesn't exist"


@app.get("/completed_tasks/{username}")
def get_completed_tasks(task_id: int, username: str):
    completed_task = []
    if username in tasks_for_user:
        tasks_list = tasks_for_user.get(username)
        for task in tasks_for_user:
            if task.completed == True:
                completed_task.append(task)
        return completed_task
    return "user doesn't exist"
