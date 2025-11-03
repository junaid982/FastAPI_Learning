
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from fastapi import Request


app = FastAPI(name = "JWT Authentication")


app.mount("/static" , StaticFiles(directory="static") , name="static")
app.mount("/media" , StaticFiles(directory="media") , name="media")


templates = Jinja2Templates(directory="templates")



@app.get("/")
async def login_view(request : Request):
    """
    This Function is used to render a login page  
    """
    
    return templates.TemplateResponse("login.html" , {"request" : request})



@app.get("/dashboard")
async def dashboard_view(request : Request):
    """
    This Function is used to render the dashboard page
    """
    
    return templates.TemplateResponse("dashboard.html" , {"request" : request})