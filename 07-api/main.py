import pickle
import pandas as pd
import uvicorn
import os

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

def load_pickle_file(path, description):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{description} file not found at path: {path}")
    with open(path, "rb") as f:
        return pickle.load(f)

MODEL_PATH = "./modelo/rf.pkl"
model = load_pickle_file(MODEL_PATH, "Model")

COLUMNS_PATH = "./modelo/data_columns.pickle"
ohe_tr = load_pickle_file(COLUMNS_PATH, "Columns info")

BINS_PH_PATH = './modelo/saved_bins_ph.pickle'
new_saved_bins_ph = load_pickle_file(BINS_PH_PATH, "Bins for PH")

BINS_SULFATE_PATH = './modelo/saved_bins_sulfate.pickle'
new_saved_bins_sulfate = load_pickle_file(BINS_SULFATE_PATH, "Bins for Sulfate")

BINS_TRIHALOMETHANES_PATH = './modelo/saved_bins_trihalomethanes.pickle'
new_saved_bins_trihalomethanes = load_pickle_file(BINS_TRIHALOMETHANES_PATH, "Bins for Trihalomethanes")

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
async def root(): #Async permite que la respuesta sea asíncrona, la respuesta puede demorar. Por lo tanto, el cliente debe preparar su código para esperar.
    return {"message": "Grupo 02 levantando su primera API"}

@app.post("/prediccion")
def predict_water_potability(answer: Answer):
# def predict_water_potability(answer: list[Answer]): #Para recibir arreglos de data

    answer_dict = jsonable_encoder(answer)
    # answer_dict = [jsonable_encoder(item) for item in answer]
    
    for key, value in answer_dict.items():
        answer_dict[key] = [value]
    
    single_instance = pd.DataFrame.from_dict(answer_dict)

    single_instance["ph"] = single_instance["ph"].astype(float)
    single_instance["ph"] = pd.cut(single_instance["ph"], new_saved_bins_ph, include_lowest=True)
    
    single_instance["Sulfate"] = single_instance["Sulfate"].astype(float)
    single_instance["Sulfate"] = pd.cut(single_instance["Sulfate"], new_saved_bins_sulfate, include_lowest=True)

    single_instance["Trihalomethanes"] = single_instance["Trihalomethanes"].astype(float)
    single_instance["Trihalomethanes"] = pd.cut(single_instance["Trihalomethanes"], new_saved_bins_trihalomethanes, include_lowest=True)

    single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)
    prediction = model.predict(single_instance_ohe)
    
    score = int(prediction[0])
    # score = prediction.tolist()

    response = { "score": score }

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)