import bcrypt

import asyncio


ALGORITH = "HS256"




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