

# Step 1 import required Libraries
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request


# Step 2 configure app and template directory 

app = FastAPI(name = "render html") 

templates = Jinja2Templates(directory="templates")


# Step 3 Create rendering function 
@app.get("/")
async def index_view(request : Request):
    """
    This function is used to render the templates
    """
    
    return templates.TemplateResponse("index.html" , {"request" : request})
