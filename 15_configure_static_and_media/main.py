
from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(name="render html with static and media")

app.mount("/static",StaticFiles(directory="static") , name="static")
app.mount("/media",StaticFiles(directory="media") , name="media")


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index_view(request : Request ):
    """
    This function is used to render html file 
    """
    
    return templates.TemplateResponse("index.html" , {"request" : request})