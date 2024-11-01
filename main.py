"""
Demo social network API
Developed by Abdurahman Airan
Development start at 03.08.2024
"""
from fastapi import FastAPI
from users.router import users_router
from messages.router import messages_router
from pages.router import templates_router

app = FastAPI(title="ChatAPI", root_path='/api/v1')

app.include_router(users_router, prefix='/users', tags=["Users"])
app.include_router(messages_router, prefix='/messages', tags=[""])
app.include_router(templates_router)