import pandas as pd
import pickle
import uvicorn

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = "" # Completar

# Completar
# with open(MODEL_PATH, "rb") as f:
#     model = pickle.load(f)
    
class Answer(BaseModel):  # Completar
    campo_ejemplo: float
    # Add more fields as needed

@app.get("/")
async def root():
    return {"message": "Grupo 02 levantando su primera API"}

@app.post("/")
def predict(answer: Answer): # Completar
    return {"message": "Completar"} # Completar

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)