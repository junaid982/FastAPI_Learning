
# command to run 
# >>> fastapi dev main.py 


from fastapi import FastAPI


app = FastAPI(name = "path converter" )


# this api can not accept the path bydefault "/var/www/html/project/media/text.txt" 

# API cURL
'''
http://127.0.0.1:8000/files//var/www/html/project/media/text.txt

'''

@app.get("/files/{file_path}")
async def store_file_path(file_path : str):
    
    return {
        "message" : f"this is file path : {file_path}"
    }
    
    


# This API Will Allow the file path such as  "/var/www/html/project/media/text.txt" 
# this will help you when you are taking file path as input 

@app.get("/get/file/path/{file_path:path}")  # here just add : path # it will automatically accept the path  
async def get_file_path(file_path : str):
    
    return {
        "messgae" : f"This is file path : {file_path}"
    }




