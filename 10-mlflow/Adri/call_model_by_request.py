import requests

"""
Recordar levantar el server, por ejemplo en el puerto 1234 de la siguiente manera:
mlflow models serve --model-uri "runs:/< TU RUN ID>/<NOMBRE DE TU MODELO>" -p 1234 --no-conda

Como por ejemplo:
mlflow models serve --model-uri 'runs:/7f2fbef44f5a4b1e9d47a46108d30140/primer_run_rf' -p 1234 --no-conda
"""

url = 'http://127.0.0.1:1234/invocations'
#url = 'https://magical-belen-nonvituperatively.ngrok-free.dev/invocations'

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

request_data = {
    "dataframe_records": aux_data
}

response = requests.post(url,json=request_data, timeout=10)
print (response.json())


