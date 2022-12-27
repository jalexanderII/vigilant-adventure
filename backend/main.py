from typing import List
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConnectionManager:
    def __init__(self)->None:
        self.active_connections: List[WebSocket] = []

        async def connect(self, websocket: WebSocket):
            await websocket.accept()
            self.active_connections.append(websocket)

            def disconnect(self, websocket:WebSocket):
                self.active_connections.remove(websocket)

                async def send_personal_message(self, message: str, websocket: WebSocket):
                    await websocket.send_text(message)

                    async def broadcast(self, message: str):
                        for connection in self.active_connections:
                            await connection.send_text(message)


