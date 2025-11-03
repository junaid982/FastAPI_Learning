

import bcrypt
import asyncio
from jose import jwt , ExpiredSignatureError , JWSError
from fastapi import status
from datetime import datetime , timedelta
from fastapi import Request, Response , HTTPException


# encrypt password 

ALGORITH = "HS256"


# 1 - Encrypt Password
async def encrypt_password(password):
    
    hash_password = bcrypt.hashpw(password.encode("utf-8") , bcrypt.gensalt() ).decode("utf-8")
    return hash_password



# 2 - Verify Encrypted Password
async def verify_password(password , hash_password):
    
    validate =  bcrypt.checkpw(password.encode("utf-8") , hash_password.encode("utf-8"))

    return validate






# 3 - Create JWT Token 

ACCESS_TOKEN_KEY = "accesstokensecretkey1234"
REFRESH_TOKEN_KEY = "refreshtokensecretkey1234"

ACCESS_TOKEN_EXPIRE_MINUTES = 1
REFRESH_TOKEN_EXPIRE_DAYS = 2

async def create_token(data : dict ,token_type : str ):
    
    token_expiry = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data["exp"] = token_expiry
    
    if token_type == "access_token":

        token = jwt.encode(data , ACCESS_TOKEN_KEY , algorithm=ALGORITH )
    
    elif token_type == "refresh_token":
        
        token = jwt.encode(data , REFRESH_TOKEN_KEY , algorithm=ALGORITH)
    
    else:
        raise ValueError("Invalid token type : 'access_token' or 'refresh_token'")
    
    
    return token







# validate token 
async def validate_token(token):
    
    try:
        payload = jwt.decode(token , key=ACCESS_TOKEN_KEY , algorithms=ALGORITH)
        return payload

    except ExpiredSignatureError:
        return None
    except JWSError:
        return None


