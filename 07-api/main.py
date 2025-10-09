import pickle
import pandas as pd
import uvicorn

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = "./modelo/rf.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
  
COLUMNS_PATH = "./modelo/data_columns.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)

BINS_PH_PATH = './modelo/saved_bins_ph.pickle'
with open(BINS_PH_PATH, 'rb') as handle:
    new_saved_bins_ph = pickle.load(handle)

BINS_SULFATE_PATH = './modelo/saved_bins_sulfate.pickle'
with open(BINS_SULFATE_PATH, 'rb') as handle:
    new_saved_bins_sulfate = pickle.load(handle)

BINS_TRIHALOMETHANES_PATH = './modelo/saved_bins_trihalomethanes.pickle'
with open(BINS_TRIHALOMETHANES_PATH, 'rb') as handle:
    new_saved_bins_trihalomethanes = pickle.load(handle)

class Answer(BaseModel):
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
def predict_water_potability(answer: Answer):

    answer_dict = jsonable_encoder(answer)
    
    for key, value in answer_dict.items():
        answer_dict[key] = [value]
    
    single_instance = pd.DataFrame.from_dict(answer_dict)

    single_instance["ph"] = single_instance["ph"].astype(float)
    single_instance["ph"] = pd.cut(single_instance["ph"], new_saved_bins_ph, include_lowest=True)
    
    single_instance["Sulfate"] = single_instance["Sulfate"].astype(float)
    single_instance["Sulfate"] = pd.cut(single_instance["Sulfate"], new_saved_bins_sulfate, include_lowest=True)

    single_instance["Trihalomethanes"] = single_instance["Trihalomethanes"].astype(float)
    single_instance["Trihalomethanes"] = pd.cut(single_instance["Trihalomethanes"], new_saved_bins_sulfate, include_lowest=True)

    single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)
    prediction = model.predict(single_instance_ohe)
    
    score = int(prediction[0])

    response = { "score": score }

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)