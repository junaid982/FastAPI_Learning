
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(name = "render_templates")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index_view(request : Request):
    """
    This method is used to render html file 
    """
    
    return templates.TemplateResponse("index.html" , {"request" : request})