from smtplib import SMTP
from pydantic_settings import BaseSettings
from enum import Enum

class Settings(BaseSettings):
    authjwt_secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    DB_HOST: str = "localhost"
    DB_NAME: str = "citymultibot"
    DB_USER: str = "citymultibot"
    DB_PASSWORD: str = "2V2wEzxb2EISSvJk"
    ALGORITHM: str = "HS256"

""" mailconf = ConnectionConfig(
    MAIL_USERNAME ="airan1999@mail.ru",
    MAIL_PASSWORD = "eJXAdKKaxzVB8a98Gbqj",
    MAIL_FROM = "airan1999@mail.ru",
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.mail.ru",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
) """

settings = Settings()

class DBSettings:
    SQLALCHEMY_DATABASE_URL = f"mysql+aiomysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"