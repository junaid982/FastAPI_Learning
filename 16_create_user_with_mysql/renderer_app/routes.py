
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/register")
async def register_view(request : Request):
    
    return templates.TemplateResponse("register.html" , {"request" : request})