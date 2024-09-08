import os
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from dotenv import load_dotenv
from middlewares.error_handler import ErrorHandler
from users.router import user_router

app = FastAPI()
app.title = "Emails aplication"


app.add_middleware(ErrorHandler)
app.include_router(user_router)
