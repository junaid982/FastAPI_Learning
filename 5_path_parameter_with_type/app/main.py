
# command to run 
# >>> fastapi dev main.py 


from fastapi import FastAPI

app = FastAPI(name = "Path Parameter with Type")


@app.get("/")
async def index():
    
    return {
        "message" : "Path Parameter with type in FastAPI ,"
    }  
    
    

@app.get("/get_data/without_type/{id}")
async def get_data(id):
    
    if isinstance(id , int):
        print(f"id is integer : {id}")
        return {
            "message" : f"id is integer : {id}"
        }
        
    else:
        print("id is not int")
        return {
            "message" : f"id is not int"
        }
        
        
@app.get("/get_data/with_type/{id}")
async def get_typed_data(id : int):
    
    if isinstance(id , int):
        return {
            "message" : f"id : {id} is int"
        }
        
    else:
        return {
            "message" : f"id : {id} is not int "
        }