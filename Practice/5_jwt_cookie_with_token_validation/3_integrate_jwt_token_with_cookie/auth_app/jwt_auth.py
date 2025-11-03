import bcrypt

from jose import jwt , JWSError , ExpiredSignatureError
from datetime import datetime , timedelta

import asyncio


ALGORITH = "HS256"
ACCESS_COOKIE_NAME = "access_token"
REFRESH_COOKIE_NAME = "refresh_token"

ACCESS_TOKEN_SECRET_KEY = "accesstokensecretkey1234"
REFRESH_TOKEN_SECRET_KEY = "refreshtokensecretkey1234"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAY = 7



# 1 - hash password
async def encrypt_password(password : str):
    
    """
    This Function is used to hash password
    """
    
    byte_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    response = bcrypt.hashpw(byte_password , salt).decode("utf-8")

    return response
    
    
    
    
    
    
# 2 - Validate Password
async def validate_password(password : str , hash_password : str):
    """
    This Function is used to Validate Password 
    """
    
    bytes_password = password.encode("utf-8")
    bytes_hash_password = hash_password.encode("utf-8")
    response  = bcrypt.checkpw(bytes_password ,bytes_hash_password )

    return response




# 3 - Create JWT token 
async def create_token(data : dict , token_type : str):
    
    
    
    if token_type == "access_token":
        expires_time = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
        data['exp'] = expires_time
        
        token = jwt.encode(data , ACCESS_TOKEN_SECRET_KEY , algorithm=ALGORITH)
        
    elif  token_type == "refresh_token":
        expires_day = datetime.utcnow() + timedelta(days = REFRESH_TOKEN_EXPIRE_DAY)
        data['exp'] = expires_day
        
        token = jwt.encode(data , REFRESH_TOKEN_SECRET_KEY , algorithm=ALGORITH)
    
    
    else:
        raise ValueError("Invalid token_type ,token_type 'access_token' or 'refresh_token'")
    
    
    return token



# 4 - Validate Token 

async def validate_token(token):
    try:
        payload = jwt.decode(token , ACCESS_TOKEN_SECRET_KEY , algorithms=[ALGORITH])
        
        return payload
    
    except JWSError:
        return None
    
    except ExpiredSignatureError:
        return None