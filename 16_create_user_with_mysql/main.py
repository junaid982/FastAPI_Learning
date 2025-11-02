from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from helpers.logging_config import setup_logger

from renderer_app.routes import router as renderer_router
from auth_app.router import router as authapi_router

app = FastAPI(name = "Create User API with MySQL")


main_logger = setup_logger("main.log")

app.mount('/static' , StaticFiles(directory="static") , name="static")
app.mount("/media" ,StaticFiles(directory="media") , name = "media")


templates = Jinja2Templates(directory="templates")

app.include_router(renderer_router  , tags=['HTML_Renders'])

app.include_router(authapi_router , prefix="/api/auth" , tags=["Auth API"])


@app.get("/")
async def login_view(request :Request ):
    main_logger.info("Render login.html")
    
    return templates.TemplateResponse("login.html" , {"request" : request})