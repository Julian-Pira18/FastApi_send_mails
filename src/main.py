import os
from fastapi import FastAPI
from src.middlewares.error_handler import ErrorHandler
from src.users.router import user_router
import uvicorn


app = FastAPI()
app.title = "Emails aplication"


app.add_middleware(ErrorHandler)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(app)
