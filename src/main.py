import os
from fastapi import FastAPI
from src.middlewares.error_handler import ErrorHandler
from src.users.router import user_router
import uvicorn
from src.models import users, course, event
# import src.models.users
from src.config.database import Base, engine

app = FastAPI()
app.title = "Emails aplication"


app.add_middleware(ErrorHandler)
app.include_router(user_router)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app)
