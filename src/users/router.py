from fastapi_mail import FastMail, MessageSchema
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from src.users.schemas import EmailSchema, Users
from src.config.mail import conf
from src.templates.register import template_password, template_register
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.utils.generate_password import generate_password
from pydantic import EmailStr
from typing import List
from src.models import *
user_router = APIRouter()


@user_router.get("/")
async def hello():
    return "Hello World"


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


@user_router.post("/send_mass_email/", tags=["Email students"])
async def send_mass_email(event_name: str, subject: str, content: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    event = db.query(Event).filter(
        Event.name == event_name).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    course = db.query(Course).filter(Course.id == event.course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    users = db.query(User).join(user_course, user_course.c.user_id == User.id).filter(
        user_course.c.course_id == course.id).all()

    emails = [user.email for user in users]

    message = MessageSchema(
        subject=subject,
        recipients=emails,
        body=content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Emails sent successfully"}


#  Password reset.
@user_router.post("/send_password_reset/", tags=["Email students"])
async def send_password_reset(email: List[EmailStr], background_tasks: BackgroundTasks):
    reset_link = "LINK"
    email_content = template_password(reset_link)

    message = MessageSchema(
        subject="Reset Password",
        recipients=email,
        body=email_content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Emails sent successfully"}


@user_router.post("/send_registration_email/", tags=['Email students'])
async def send_registration_email(user_data: Users, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
        Sends a registration email to a new user asynchronously.

        This function creates a personalized registration email for the user with
        their name and password, then sends the email in the background using FastMail.

        Parameters:
        ----------
        email_data : EmailSchema
            Contains the subject and recipient(s) for the email.
        name : str
            The name of the user to personalize the email content.

        password : str
            The password for the new user, to be included in the email content.
        background_tasks : BackgroundTasks
            Background task manager to handle sending the email asynchronously.

        Returns:
        -------
        dict
            A message indicating that the registration email was sent successfully.

        Example:
        --------
        await send_registration_email(email_data, "John Doe", "johndoe", "mypassword", background_tasks)
    """

    username = f"{user_data.name} {user_data.lastname}"
    password = generate_password(user_data.name, user_data.lastname)
    email_content = template_register(
        username, password)

    new_user = User(name=user_data.name,
                    lastname=user_data.lastname, email=user_data.email, password=password, photo_url="x", role_id="student")

    db.add(new_user)
    db.commit()
    message = MessageSchema(
        subject=f"Welcome {username}",
        recipients=user_data.email,
        body=email_content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Registration email sent successfully"}
