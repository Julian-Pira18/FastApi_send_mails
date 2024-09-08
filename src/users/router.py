import os
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from middlewares.error_handler import ErrorHandler
from fastapi import APIRouter
from users.schemas import EmailSchema, conf

user_router = APIRouter()


@user_router.post("/send_email/")
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


@user_router.post("/send_mass_email/")
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
@user_router.post("/send_password_reset/", tags=["Email for students"])
async def send_password_reset(email_data: EmailSchema, name: str, reset_link: str, background_tasks: BackgroundTasks):

    email_content = f"""
    <html>
        <body>
            <h2>Hello {name},</h2>
            <p>We have received a request to reset the password for your account. If you did not make this request, you can safely ignore this email.</ p>
            <p>To reset your password, simply click on the following link or copy and paste the URL into your browser:</p>
            <p><a href="{reset_link}">{reset_link}</a></p>
            <p>If you have any questions or need further assistance, please feel free to contact us.</p>
            <p>Thank you,</p>
        </body>
    </html>
"""
    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Emails sent successfully"}

# Resgitro de un nuevo usuario.


@user_router.post("/send_registration_email/", tags=['Email for new students'])
async def send_registration_email(email_data: EmailSchema, name: str, user: str, password: str, background_tasks: BackgroundTasks):
    email_content = f"""
<html>
<body>
    <h1>Welcome {name}!</h1>
    <p>We are excited to have you on board. Your account has been successfully created. Below are your temporary login credentials:</p>
    <p><strong>Username:</strong> {user}</p>
    <p><strong>Password:</strong> {password}</p>
    <p>We recommend changing your password as soon as you log in for the first time.</p>
    <p>If you have any questions or need assistance, feel free to contact our support team.</p>
    <p>Thank you for joining us!</p>
</body>
</html>
"""

    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_content,
        subtype="html"
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Registration email sent successfully"}
