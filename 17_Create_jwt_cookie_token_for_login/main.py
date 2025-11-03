
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import RedirectResponse

from auth_app.routers import router as auth_router


app = FastAPI(name = "Create JWT Token")


app.mount("/static" , StaticFiles(directory="static") , name="static")
app.mount("/media" , StaticFiles(directory="media") , name="media")


templates = Jinja2Templates(directory="templates")


app.include_router(auth_router , prefix="/api/auth" , tags=['Auth API'])


@app.get("/")
async def login_view(request : Request):
    
    return templates.TemplateResponse("login.html" , {"request" : request})




@app.get("/dashboard")
async def dashboard_view(request : Request):
    
    return templates.TemplateResponse("dashboard.html" , {"request" : request})


