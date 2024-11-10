"""
Demo social network API
Developed by Abdurahman Airan
Development start at 03.08.2024
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from users.router import users_router
from messages.router import messages_router
from pages.router import templates_router

app = FastAPI(title="ChatAPI", root_path='/api/v1')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix='/users', tags=["Users"])
app.include_router(messages_router, prefix='/messages', tags=[""])
app.include_router(templates_router)