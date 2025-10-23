

# Run Command 
# >>> fastapi dev main.py


from fastapi import FastAPI

app = FastAPI(name = "project Structure")


@app.get("/")
def index():
    return {
        "message" : "Hello Fast API"
    }