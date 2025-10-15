from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel
import pickle
import pandas as pd
from fastapi.encoders import jsonable_encoder


app = FastAPI()

# Modelo
MODEL_PATH = "model/rf.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Columnas
COLUMNS_PATH = "model/categories_ohe.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)

# Bins
BINS_PH = 'model/saved_bins_ph.pickle'
with open(BINS_PH, 'rb') as handle:
    new_saved_bins_ph = pickle.load(handle)

BINS_SULFATE = 'model/saved_bins_sulfate.pickle'
with open(BINS_SULFATE, 'rb') as handle:
    new_saved_bins_sulfate = pickle.load(handle)

BINS_TRIHALOMETHANES = 'model/saved_bins_trihalomethanes.pickle'
with open(BINS_TRIHALOMETHANES, 'rb') as handle:
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
def root():
    return {"message": "Proyecto para Bootcamp de EDVAI"}


@app.post("/prediccion")
def predict_water_potability(answer: Answer):

    answer_dict = jsonable_encoder(answer)
    
    for key, value in answer_dict.items():
        answer_dict[key] = [value]
    
    # Crear dataframe
    single_instance = pd.DataFrame.from_dict(answer_dict)

    # Manejar puntos de corte o bins
    single_instance["ph"] = single_instance["ph"].astype(float)
    single_instance["ph"] = pd.cut(single_instance['ph'],
                                     bins=new_saved_bins_ph, 
                                     include_lowest=True)
    
    single_instance["Sulfate"] = single_instance["Sulfate"].astype(float)
    single_instance["Sulfate"] = pd.cut(single_instance['Sulfate'],
                                     bins=new_saved_bins_sulfate, 
                                     include_lowest=True)
    
    single_instance["Trihalomethanes"] = single_instance["Trihalomethanes"].astype(float)
    single_instance["Trihalomethanes"] = pd.cut(single_instance['Trihalomethanes'],
                                     bins=new_saved_bins_trihalomethanes, 
                                     include_lowest=True)

    # One hot encoding
    single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)
    
    prediction = model.predict(single_instance_ohe)
    # Cast numpy.int64 to just a int
    score = int(prediction[0])
    
    response = {"score": score}
    
    return response


# Corre en http://127.0.0.1:8000 o http://0.0.0.0:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
