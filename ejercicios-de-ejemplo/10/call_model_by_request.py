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
Age = 34
EmploymentType = 1
GraduateOrNot = 1
AnnualIncome = 500000
FamilyMembers = 4
ChronicDiseases = 1
FrequentFlyer = 0
EverTravelledAbroad = 0

data = [[Age, EmploymentType, GraduateOrNot, AnnualIncome, FamilyMembers, ChronicDiseases, FrequentFlyer, EverTravelledAbroad]]

request_data = {
    "dataframe_records": data
}

response = requests.post(url,json=request_data, timeout=10)
print (response.json())


