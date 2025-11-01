import pandas as pd
import mlflow

# Reemplazar por tu RUN ID
# logged_model = 'runs:/< TU RUN ID>/< NOMBRE DE TU MODELO>'
logged_model = 'runs:/640c14c9368e4f4398b67c06b951a085/mi_modelo'
#file:///Users/cosmos/Adri/Developer/DataScience/Clases%20y%20Consignas/Clase%2011%20EDVai%20MLFlow/Tarea%20MLFlow/mlruns/633329904184795514/9ecd5e03237e45b8b154e3bc40d319f4/artifacts/model.pkl

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Input data
Air_temperature	= 298.9
Process_temperature	= 309.1
Rotational_speed = 2861
Torque = 4.6
Tool_wear = 143
Type_H = 1 
Type_L = 0 
Type_M = 0

aux_data = [[Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Type_H, Type_L, Type_M]]


# Construye el DataFrame con dtype=object (coincide con la firma que grabaste)
## Lo hacemos porque tenemos una mezcla de tipo de datos por el One Hot Encoding
## Este paso solo es para el call_model_by_run_id
data = pd.DataFrame(aux_data, dtype=object)

# Predict on a Pandas DataFrame.
response = loaded_model.predict(pd.DataFrame(data))
print(response)
