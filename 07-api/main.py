import pandas as pd
import pickle
import uvicorn

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = "07-api/modelo/rf.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
  
COLUMNS_PATH = "07-api/modelo/data_columns.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)

BINS_PH_PATH = '07-api/modelo/saved_bins_ph.pickle'
with open(BINS_PH_PATH, 'rb') as handle:
    new_saved_bins_ph = pickle.load(handle)

BINS_SULFATE_PATH = '07-api/modelo/saved_bins_sulfate.pickle'
with open(BINS_SULFATE_PATH, 'rb') as handle:
    new_saved_bins_sulfate = pickle.load(handle)

BINS_TRIHALOMETHANES_PATH = '07-api/modelo/saved_bins_trihalomethanes.pickle'
with open(BINS_TRIHALOMETHANES_PATH, 'rb') as handle:
    new_saved_bins_trihalomethanes = pickle.load(handle)

class Answer(BaseModel):  # Completar
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

@app.get("/")
async def root():
    return {"message": "Grupo 02 levantando su primera API"}

@app.post("/prediccion")
def predict_water_potability(answer: Answer): # Completar
    return {"message": "Completar"} # Completar

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)