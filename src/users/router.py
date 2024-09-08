from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema

from fastapi import APIRouter
from src.users.schemas import EmailSchema
from src.config.mail import conf
from src.templates.register import template_password, template_register
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


@user_router.post("/send_mass_email/", tags=["Email students"])
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


#  Password reset.
@user_router.post("/send_password_reset/", tags=["Email students"])
async def send_password_reset(email_data: EmailSchema, name: str, reset_link: str, background_tasks: BackgroundTasks):

    email_content = template_password(name, reset_link)

    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Emails sent successfully"}

# Resgiter of a new user.


@user_router.post("/send_registration_email/", tags=['Email students'])
async def send_registration_email(email_data: EmailSchema, name: str,  password: str, background_tasks: BackgroundTasks):
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
    email_content = template_register(name, password)

    message = MessageSchema(
        subject=email_data.subject,
        recipients=email_data.email,
        body=email_content,
        subtype="html"
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
    return {"message": "Registration email sent successfully"}
