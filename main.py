import os
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv('.env')

mail_passsword = os.getenv("MAIL_PASSWORD")


class EmailSchema(BaseModel):
    email: List[EmailStr]
    subject: str
    content: str
    
conf = ConnectionConfig(
    MAIL_USERNAME ="jpira.dev@gmail.com",
    MAIL_PASSWORD = mail_passsword,
    MAIL_FROM = "jpira.dev@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,  # SSL should be False for port 587
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
)

class User(BaseModel):
    username: str
    name: str
    lastname: str
    subject: str
    content: str

app = FastAPI()

@app.post("/send_email/")
async def send_email(email_data: EmailSchema, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_data.content,
        subtype="html"
    )
    
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Email sent successfully"}

@app.post("/send_mass_email/")
async def send_mass_email(email_data: EmailSchema, background_tasks: BackgroundTasks):
    
    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_data.content,
        subtype="html"
    )
    
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Emails sent successfully"}



# Restablecimiento de contraseña. 
@app.post("/send_password_reset/")
async def send_mass_email(email_data: EmailSchema, background_tasks: BackgroundTasks):
    
    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_data.content,
        subtype="html"
    )
    
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Emails sent successfully"}


