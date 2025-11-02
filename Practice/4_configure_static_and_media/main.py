
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(name = "render html with static and media")

app.mount("/static" , StaticFiles(directory="static") , name = "static")
app.mount("/media" , StaticFiles(directory = "media") , name = "media")


templates = Jinja2Templates(directory = "templates")


@app.get("/")
async def index_view(request : Request):
    
    
    return templates.TemplateResponse("index.html" , {"request" : request})