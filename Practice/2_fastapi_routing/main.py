
from fastapi import FastAPI
from user.routers import router as user_router


app = FastAPI(name = "FastAPI_Routing")

app.include_router(user_router , prefix="/api/user" , tags=["users"])

