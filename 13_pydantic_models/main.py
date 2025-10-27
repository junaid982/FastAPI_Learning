from fastapi import FastAPI

from helpers.logging_config import setup_logger


logger = setup_logger("main.log")

app = FastAPI(name = "Pydantic Models")

# This API is used to Understand the Pydantic models 

# 1 - Simple Pydantic Models
# 2 - Multiple Pydantic Models
# 3 - Pydantic Fields
# 4 - Nested Pydantic Body


# What is Pydantic 
# pydantic is python library which is used to validate the request and response json body data in fastapi 


# ------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Simple Pydantic Models

# a - without pydantic validation


USERS = []

# This is working perfectly but limitation is there is validation on request data .
# user can pass anything in this json or dict body we have to create custom logic for json body validation

# curl Example

'''
Exampel 1

curl --location 'http://127.0.0.1:8000/add/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id" : 1,
    "name" : "Junaid",
    "email" : "junaid@gmail.com"
}'


Example 2

curl --location 'http://127.0.0.1:8000/add/users' \
--header 'Content-Type: application/json' \
--data '{
    "id" : "id no 2",
    "fullname"  :10,
    "email" : 101
}'

'''

@app.post("/add/users")
async def add_user(user : dict):
    """
    This API is used to get the Json ( dict ) body as request
    """
    
    logger.info("add_user API Called .")
    logger.info("Dict Data recieved .")
    
    USERS.append(user)
    logger.info("Request Data added to the USERS list.\n")
    
    return {
        "message" : "User Created successfully."
    }
    
    




# b - with pydantic validation

# In this API we are going to use Pydantic for typing validation 


# This API is with typing validation 
# user can only pass these added fields only to the request body and same type also 
# otherwise it gets error 

# Example curl
'''

'''



from pydantic import BaseModel

class UserModel(BaseModel):
    id : int
    name : str
    email : str
    contact : int



@app.post("/create/user")
async def create_user(user : UserModel):
    """
    This API is used to store the request user data into the list with typing validation with pydantic 
    """
    
    USERS.append(user)
    
    return {
        "message" : "User Created Successfully"
    }


 
# ------------------------------------------------------------------------------------------------------------------------------------------


# 2 - Multiple Pydantic Models


