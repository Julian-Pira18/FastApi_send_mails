from fastapi_mail import FastMail, MessageSchema
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from src.users.schemas import EmailSchema, Users
from src.config.mail import conf
from src.templates.register import template_password, template_register
from sqlalchemy.orm import Session
from src.config.database import get_db
# Importar el modelo Course
from src.utils.generate_password import generate_password
from pydantic import EmailStr
from typing import List
from src.models import User
from src.models import Course
from src.models import Event as Event_model
from src.models import user_course
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

#   "error": "Could not locate a bind configured on mapper Mapper[Event(event)], SQL expression or this Session."


@user_router.post("/send_mass_email/", tags=["Email students"])
async def send_mass_email(event_name: str, subject: str, content: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    event = db.query(Event_model).filter(
        Event_model.name == event_name).first()
    print(event)
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

# Resgiter of a new user.


@user_router.post("/send_registration_email/", tags=['Email students'])
async def send_registration_email(user_data: Users, background_tasks: BackgroundTasks):
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
    email_content = template_register(
        username, generate_password(user_data.name, user_data.lastname))

    message = MessageSchema(
        subject=f"Welcome {username}",
        recipients=user_data.email,
        body=email_content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Registration email sent successfully"}
