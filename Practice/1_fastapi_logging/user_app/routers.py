

from fastapi import APIRouter
from helpers.logging_config import setup_logger

router = APIRouter()


user_logger = setup_logger("user_logger.log")

USERS = [
    {
        "id" :1,
        "name":"Junaid Ansari",
        "contact" : "9876543210",
        "email" : "junaidansari@xyz.com",
        "password" : "abc@123"
    }
]

@router.get("/get/all")
async def get_all_users():
    """
    This API is used to get all the users
    """
    
    user_logger.info("Get All user API Called .")
    user_logger.info("Send All User Data as Response.\n")
    
    return USERS