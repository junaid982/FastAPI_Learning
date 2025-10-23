



# Command to Run
# >>> fastapi dev main.py

# For Documentation 
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc




from fastapi import FastAPI


app = FastAPI( name = "First App")



@app.get("/")
async def index():
    """
    This is First APP 
    """
    
    return {
        "message" : "Hello Fast API"
    }
    
    
    