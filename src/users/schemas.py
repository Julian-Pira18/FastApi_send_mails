import os
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from middlewares.error_handler import ErrorHandler
from fastapi import APIRouter
from dotenv import load_dotenv

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../'))
dotenv_path = os.path.join(project_root, '.env')

load_dotenv(dotenv_path=dotenv_path)
mail_password = os.getenv("MAIL_PASSWORD")

print(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), '.env'))
print(f"MAIL_PASSWORD: {mail_password} \n \n \n")


class EmailSchema(BaseModel):
    email: List[EmailStr]
    subject: str
    content: str


conf = ConnectionConfig(
    MAIL_USERNAME="jpira.dev@gmail.com",
    MAIL_PASSWORD=mail_password,
    MAIL_FROM="jpira.dev@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,  # SSL should be False for port 587
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)
