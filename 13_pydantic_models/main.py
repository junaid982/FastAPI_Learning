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
    
    logger.info("Storing User data from pydantic .\n")
    USERS.append(user)
    
    return {
        "message" : "User Created Successfully"
    }


 
# ------------------------------------------------------------------------------------------------------------------------------------------


# 2 - Multiple Pydantic Models


# In this Example we are going to lean how to take multiple of pydantic model 


'''
# Example curl


curl 1  - api with all values

curl -X 'POST' \
  'http://127.0.0.1:8000/store/user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_info": {
    "name": "Junaid",
    "email": "junaid@gmail.com",
    "contact": 9876543567
  },
  "profesional_info": {
    "emp_id": "emp1234",
    "designation": "Software Engineer",
    "location": "mumbai"
  }
}'




curl 2  - to check empty and default values 

curl --location 'http://127.0.0.1:8000/store/user' \
--header 'Content-Type: application/json' \
--data-raw '{
  "user_info": {
    "name": "Junaid",
    "email": "junaid@gmail.com"
  },
  "profesional_info": {
    "emp_id": "emp123",
    "designation": "Software Engineer"
  }
}'



'''

from pydantic import BaseModel

USERS = []


class UserInfo(BaseModel):
    name : str
    email : str | None = None # make Optional
    contact : int  | None = None # Make Optional
    
class ProfessionalInfo(BaseModel):
    emp_id : str
    designation : str
    location : str | None = "mumbai"
    


@app.post("/store/user")
async def store_user(user_info : UserInfo , profesional_info : ProfessionalInfo):
    """
    This APi is used to take multiple request data 
    """
    
    logger.info("API call started.")
    logger.info("Creating Required Data to store .")
    
    # print(f"user_info : {dict(user_info)}")
    # print(f"profesional_info : {dict(profesional_info)}")
    user = {
        "user_info" :user_info,
        "profesional_info" : profesional_info
    }
    
    print(f"user : {user}")
    logger.info("Data Prepaired to store.")
    
    USERS.append(user)
    logger.info("Data Stored to the USERS list.\n")
    
    
    
    return {
        "message" : "Data stored to the list ",
        "data" : USERS
    }








 
# ------------------------------------------------------------------------------------------------------------------------------------------


# 3 - Pydantic Fields ( for better Validation)

# Pydantic provides the Field Class from which we can validate the input values without custom logic 


# Example curl
'''
curl -X 'POST' \
  'http://127.0.0.1:8000/store/user/data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "name": "string",
  "email": "string",
  "contact": "5105140872",
  "location": "mumbai"
}'
'''



from pydantic import BaseModel , Field
from enum import Enum
from typing import Optional

class LocationList(Enum):
    mumbai = "mumbai"
    chennai = "chennai"
    banglore = "banglore"

class UserData(BaseModel):
    id : int = Field(
        title="user id",
        description="user unique id",
        ge=1
    )
    
    name : str = Field(
        title="user name",
        description="user name for identification",
        min_length=2, # user name should not be less then 2 char
        max_length=20 # user name should not be greater then 20 char
    )
    
    email : str = Field(
        title="user email",
        description="user unique email for authentication",
        min_length=5, # user email should not be less then 5 char 
        max_length=50 # user email should not be greater then 50 char
    )
    
    contact : str = Field(
        title="user contact",
        description="user unique contact for authentication",
        pattern=r"^[0-9]{10}$"   # basic Reguler Expression for contact Validation ( pattern always applied on str type )
    )
    
    location : str = Field(
        title = "user location",
        description="user working location",
        default=LocationList.mumbai     # default keyword is used to add a default value
        
    ) 
    
    emp_id : str = Field(
        default=None,       # default None make it optional
        title="employee id",
        description="Employee id "
    ) 


@app.post("/store/user/data")
async def store_user_data(user : UserData):
    """
    In this API we are going to validate the request data values with pydantic Fields 
    """
    logger.info("using Pydantic Field to valilate request body data.\n")
    
    return user











# ------------------------------------------------------------------------------------------------------------------------------------------


# 4 - Nested Pydantic Body

# In this API We are going to learn how to take nested requesy body using Pydantic 

# Example Curl
'''
curl -X 'POST' \
  'http://127.0.0.1:8000/get/user/information' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Junaid Ansari",
  "email": "Email",
  "contact": "9876548765",
  "prof_info": {
    "emp_id": "emp1234",
    "designation": "Software Engineer",
    "role": "Team Lead",
    "location": "mumbai"
  }
}'
'''

from pydantic import BaseModel


class ProfInformation(BaseModel):
    emp_id : str
    designation : str
    role : str | None = "Team Lead"
    location : str | None = "mumbai"
    
class UserInformation(BaseModel):
    name : str
    email : str 
    contact : str
    prof_info : ProfInformation
    

@app.post("/get/user/information")
async def get_user_information(user_info : UserInformation ):
    
    """
    In this API we are going to learn how to take nested request body using Pydantic 
    """
    
    logger.info("API Start and get the request json body \n")
 
 
    return {
        "message" : "success",
        "data" : user_info
    }