import requests

"""
Recordar levantar el server, por ejemplo en el puerto 1234 de la siguiente manera:
mlflow models serve --model-uri "runs:/deb28e98e6944d469e7a9b762c92df9f/random_forest_model" -p 8000 --no-conda
"""

# URL
url = "http://127.0.0.1:8000/invocations"

# Body data
Air_temperature	= 298.9
Process_temperature	= 309.1
Rotational_speed = 2861
Torque = 4.6
Tool_wear = 143
Type_H = 1 
Type_L = 0 
Type_M = 0

aux_data = [[Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Type_H, Type_L, Type_M]]

# aux_data = [{
#     "Air_temperature": 298.9,
#     "Process_temperature": 309.1,
#     "Rotational_speed": 2861,
#     "Torque": 4.6,
#     "Tool_wear": 143,
#     "Type_H": 1,
#     "Type_L": 0,
#     "Type_M": 0
# }]

request_data = {
    "dataframe_records": aux_data
}

response = requests.post(url, json=request_data, timeout=10)
print(response.json( ))