

from fastapi import APIRouter 
from fastapi import status , Request , Response
from fastapi.responses import JSONResponse , RedirectResponse
from helpers.db_config import connection
from aiomysql import DictCursor

from pydantic import BaseModel , Field

from auth_app.jwt_auth import validate_password , create_token

from datetime import datetime


router = APIRouter()









# ----------------------------------------------------------------------------------------------------------
# 1 - user Login


async def serialize_data(user_data : dict):
    
    for key , value in user_data.items():
        
        if isinstance(value , datetime):
            value = value.strftime("%Y-%m-%d %H:%M:%S")
            user_data[key] = value
            
    return user_data




class UserData(BaseModel):
    username : str
    password : str


@router.post("/login")
async def login_user_api(user : UserData):
    
    """
    This API is used to authenticate the user and login 
    """

    try:
        username = user.username
        password = user.password
        
        conn = await connection()
        cur = await conn.cursor(DictCursor)
        
        query = f"""
                select 
                    new_users.id,
                    new_users.name,
                    new_users.email,
                    new_users.opoid,
                    new_users_role_master.role as role,
                    new_users_designation_master.designation as designation,
                    new_users.password,
                    new_users.is_active,
                    new_users.is_delete,
                    u.name as created_by,
                    new_users.created_at,
                    new_users.updated_at
                from 
                    new_users

                JOIN new_users_role_master
                ON new_users.role =  new_users_role_master.id

                JOIN new_users_designation_master
                ON new_users.designation = new_users_designation_master.id

                JOIN new_users as u
                ON new_users.id = u.id

                where new_users.opoid = "{username}"
        """
        
        await cur.execute(query)
        
        user_data = await cur.fetchone()
        
        await cur.close()
        conn.close()
        
        
        if not user_data:
            
            return JSONResponse(
                {
                    "status" : False,
                    "message" : "User not exists."
                },status_code=status.HTTP_404_NOT_FOUND
            )
            
        else:
            
            # validate password
            hash_password = user_data.get("password")
            
            is_valid = await validate_password(password , hash_password)
            if not is_valid:
                return JSONResponse(
                    {
                        "status" : False,
                        "message" : "Invalid Password"
                    },status_code=status.HTTP_400_BAD_REQUEST
                )
                
            else:
                
                # Delete password from response data
                user_data.pop("password")
                
                # serialize data for response ( convert sql datetime to serializable type )
                
                user_data = await serialize_data(user_data) 
                
                data = {
                    "user_id" : user_data.get("id"),
                    "name" : user_data.get("name"),
                    "opoid" : user_data.get("opoid"),
                    "role" : user_data.get("role"),
                    "designation" : user_data.get("designation"),
                }
                
                # Create Access and Refresh Token 
                access_token = await create_token(data , token_type = "access_token")
                refresh_token = await create_token(data , token_type = "refresh_token")
                
                # print(f"access_token : {access_token}")
                # print(f"refresh_token : {refresh_token}")
                
                response = JSONResponse(
                    {
                        "status" : True,
                        "message" : "Login successful",
                        "data" : user_data
                    },status_code=status.HTTP_200_OK
                )
                
                response.set_cookie(
                    key="access_token" , 
                    value=access_token , 
                    max_age = 900 ,
                    # secure = True  , # Only for https  
                    secure = False  , 
                    httponly = True,
                    samesite='lax'
                    )
                response.set_cookie(
                    key="refresh_token" , 
                    value=refresh_token , 
                    max_age = 604800 ,
                    # secure = True  , # Only for https
                    secure = False  , 
                    httponly = True,
                    samesite='lax'
                    )
                
                return response 
            
            
    
    
    except Exception as e:
        print(f"Error : {e}")
        
        return JSONResponse(
            {
                "status" : False,
                "message" : "Something Went Wrong."
            },status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
        
        

@router.post("/logout")
async def logout():
    """
    This APi is used to logout user
    """
    response = RedirectResponse(url="/" , status_code=303)
    
    response.delete_cookie(key = "access_token")
    response.delete_cookie(key = "refresh_token")
    
    return response
    