"""
Demo social network API
Developed by Abdurahman Airan
Development start at 03.08.2024
"""
from fastapi import FastAPI
from users.router import users_router

app = FastAPI(root_path='/api/v1')

app.include_router(users_router, prefix='/users', tags=["Users"])