
from fastapi import FastAPI


# import routing

from user_app.routers import router as user_router


app = FastAPI(name = "FastAPI Logging and routing")

app.include_router(user_router , prefix="/api/users" ,tags=['users'])