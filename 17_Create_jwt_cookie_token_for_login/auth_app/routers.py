from fastapi import APIRouter
from fastapi.responses import JSONResponse , RedirectResponse
from fastapi import status
from fastapi import Response


from pydantic import BaseModel , Field

from aiomysql import DictCursor

from datetime import datetime

from helpers.db_config import connection

from auth_app.jwt_auth import verify_password , create_token

router = APIRouter()


class UserData(BaseModel):
    username : str
    password : str = Field(
        title="User Password",
        description="User Unique password",
        max_length=20,
        min_length=5
    )



async def serialize_data(user_data):
    
    for key,value in user_data.items():
        if isinstance(value , datetime):
            
            user_data[key] = value.strftime("%Y-%m%d %H:%M:%S")
            
    return user_data


@router.post("/login")
async def user_login(user : UserData) :
    
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
            return JSONResponse({
                "status" : False,
                "messgae" : "User does not exists.",
            },status_code=status.HTTP_404_NOT_FOUND)
            
        else:
            
            # Check Password 
            
            hash_password = user_data.get("password")
            
            password_valid = await verify_password(password , hash_password)
            
            if not password_valid:
                return JSONResponse(
                    {
                        "status" : False,
                        "message" : "Invalid Password"
                    },status_code=status.HTTP_400_BAD_REQUEST
                )
            
            
            else:
                user_data.pop("password")
                
                user_data = await serialize_data(user_data)
                
                data = {
                    "user_id" : user_data.get("id"),
                    "opoid" : user_data.get("opoid"),
                    "designation" : user_data.get("designation"),
                    "role" : user_data.get("role"),
                }
                
                access_token = await create_token(data ,"access_token" )
                refresh_token = await create_token(data ,"refresh_token" )
                
                
                
                response = JSONResponse(
                    {
                        "status" : True,
                        "messsage" : "Login Success",
                        "data" : user_data
                    },status_code=status.HTTP_200_OK
                )
                
                
                response.set_cookie(access_token , httponly = True , max_age = 900 , secure = True)
                response.set_cookie(refresh_token , httponly = True , max_age = 604800 , secure = True)
                
                return response
        
        
        
        
    except Exception as e:
        print(f"Error  : {e}")
        
        
        
    


