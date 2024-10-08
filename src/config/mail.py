import os
from fastapi_mail import ConnectionConfig
print("\n \n \n \n")
print(os.getenv("MAIL_USERNAME"))
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,  # SSL should be False for port 587
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)
