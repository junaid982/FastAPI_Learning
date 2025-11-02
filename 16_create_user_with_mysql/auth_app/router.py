from fastapi import APIRouter 
from fastapi.responses import JSONResponse
from fastapi import status
from pydantic import BaseModel , Field

import aiomysql
from aiomysql import DictCursor
from helpers.db_config import connection

from helpers.logging_config import setup_logger


router = APIRouter()

auth_api_logger = setup_logger("auth_app.log")

# --------------------------------------------------------------------------------------------------------
# 1 - API to get all the roles except Super Admin

@router.get("/get/roles")
async def get_user_roles():
    """
    This API is used to get all the roles excepts Super Admin 
    """
    auth_api_logger.info("Get user Role API CAll")
    try:
        
        conn = await connection()
        cur = await conn.cursor(DictCursor)
        
        query = """
            Select id , role from new_users_role_master where id != 1
        """
        
        await cur.execute(query)
        user_role = await cur.fetchall()
        
        # user_role = [ role.get('role') for role in user_role]
        
        
        await cur.close()
        conn.close()
       
        
        auth_api_logger.info("Data sends as response.\n")
        
        return JSONResponse(
            {
                "status" : True,
                "messgae" : "Role Data Fetched.",
                "data" : user_role
            }, 
            status_code=status.HTTP_200_OK
            )

        # return {"message" : "succes"}
    
    except Exception as e:
        
        auth_api_logger.error(f"Error : {e}\n")
        
        return JSONResponse({
            "status" : False,
            "messgae" : f"{e}"
        },
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR                
        )
    






# Get User Designation
@router.get("/get/designation")
async def get_user_designation():
    
    try:
        auth_api_logger.info(f"Get User Designation API Call Start")
        
        conn = await connection()
        cur = await conn.cursor(DictCursor)
        
        query = """
            select id , designation from new_users_designation_master
        """
        
        await cur.execute(query)
        
        user_designation = await cur.fetchall()

        # user_designation = [ designation.get("designation") for designation in user_designation]
                
        await cur.close()
        conn.close()
        
        auth_api_logger.info(f"Data sends as Response.\n")
        
        return JSONResponse(
            {
                "status" : True,
                "messgae" : "Fetch all user Designation",
                "data" : user_designation
            },
            status_code=status.HTTP_200_OK
        )
        
    except Exception as e:
        
        auth_api_logger.error(f"Error : {e}\n")
        
        return JSONResponse(
            {
                "status":False,
                "message" : f"Error : {e}"
            }
            ,status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
        
        
import bcrypt

class UserData(BaseModel):
    name : str = Field(
        title="user name",
        description="User full name",
        min_length=2,
        max_length=20
    )
    
    email : str = Field(
        title="user email",
        description="user unique email",
        pattern="^[\w\.-]+@[\w\.-]+\.\w{2,}$",
    )
    
    opoid : str 
    role : int
    designation :int 
    password : str = Field(
        title="user Password",
        description="user unique password",
        min_length=5,
        max_length=20
    )
    created_by : int


# async def encrypt_password(password : str) ->str:
#     return bcrypt.hash(password)

async def encrypt_password(password: str) -> str:
    # Convert password to bytes
    password_bytes = password.encode('utf-8')

    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    # Return decoded string for storage (optional)
    return hashed.decode('utf-8')




@router.post("/create/user")
async def create_user(user : UserData):
    # print(f"UserData : {user}")
    
    auth_api_logger.info("Create User APi Call ")
    
    try:
        hash_password = await encrypt_password(user.password)
        
        conn = await connection()
        cur = await conn.cursor(DictCursor)
        
        query = f"""
            insert into new_users (
                name,
                email,
                opoid,
                role,
                designation,
                password,
                created_by
            )
            values(
                '{user.name}' ,
                '{user.email}',
                '{user.opoid}',
                '{user.role}',
                '{user.designation}',
                '{hash_password}',
                '{user.created_by}'
                );
        """
        
        await cur.execute(query)
        await conn.commit()
        
        await cur.close()
        conn.close()
        
        
        return JSONResponse(
            {
                "status" : True,
                "message" : "user create successfully"
            },
            status_code=status.HTTP_201_CREATED
        )
        
    
    except Exception as e:
        
        auth_api_logger.error(f"Error : {e}\n")
        return JSONResponse(
            {
                "status" : False,
                "message" : f"Error : {e}"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    
    return user