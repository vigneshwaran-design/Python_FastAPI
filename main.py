from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Simple root GET route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}