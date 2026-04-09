from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dental Clinic API is running!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello Joseph!"}
