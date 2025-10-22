from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Synthetic Data Engine API is running 🚀"}
