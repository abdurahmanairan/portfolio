from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from base_schema import *
from db import get_db

templates_router = APIRouter()

templates = Jinja2Templates(directory="pages")

@templates_router.get('/', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("static/index.html", {"request": request})

@templates_router.get('/home', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("static/home.html", {"request": request})