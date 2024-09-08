import os
from fastapi_mail import ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List


class EmailSchema(BaseModel):
    email: List[EmailStr]
    subject: str
    content: str
