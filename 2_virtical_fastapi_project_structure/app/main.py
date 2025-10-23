


# Command to run 
# >>> fastapi dev main.py


from fastapi import FastAPI

app = FastAPI(name = "Project Structure")


@app.get("/")
def index():
    """
    This Code is just for demonstract how fast API Project strucre Look
    """
    
    return {
        "message" : "This Code is just for demonstract how fast API Project strucre Look"
    }
    
    