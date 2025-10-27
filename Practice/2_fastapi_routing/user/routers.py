
from fastapi import APIRouter
from helpers.logging_config import setup_logger


user_logger = setup_logger("user_logger")

router = APIRouter()



USERS = [
    {
        "id" : 1,
        "name" : "Junaid Ansari",
        "email" : "junaid@gmail.com",
        "contact" : "9876567890",
    }
]

@router.get("/get/all")
async def get_all_users():
    """
    API is used to get the All users
    """
    user_logger.info("API call started ")
    user_logger.debug("All User Data as response\n ")
    
    return USERS