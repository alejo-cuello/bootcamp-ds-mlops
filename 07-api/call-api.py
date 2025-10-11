import requests

endpoint = "prediccion"

search_api_url = "http://127.0.0.1:8000/" + endpoint

# Prueba 1 (inicial)
# data = {
#         "ph": 0,
#         "Hardness": 204.890455,
#         "Solids": 20791.318981,
#         "Chloramines": 7.300212,
#         "Sulfate": 368.516441,
#         "Conductivity": 564.308654,
#         "Organic_carbon": 10.379783,
#         "Trihalomethanes": 86.990970,
#         "Turbidity": 2.963135,
# }

# Prueba 2: resultado esperado: 0
# data = {
#     'ph': 0,
#     'Hardness': 204.890455,
#     'Solids': 20791.318981,
#     'Chloramines': 7.300212,
#     'Sulfate': 368.516441,
#     'Conductivity': 564.308654,
#     'Organic_carbon': 10.379783,
#     'Trihalomethanes': 86.990970,
#     'Turbidity': 2.963135,
# }

# Prueba 3: resultado esperado: 1
# data = {
#     'ph': 7.7984536762012135,
#     'Hardness': 188.39494231709176,
#     'Solids': 32704.569285770576,
#     'Chloramines': 11.078872478914501,
#     'Sulfate': 258.1911841475428,
#     'Conductivity': 507.1786882733106,
#     'Organic_carbon': 18.272439235274646,
#     'Trihalomethanes': 85.17766213336226,
#     'Turbidity': 4.107267203260775,
# }

# Prueba extra con registro tomado del dataframe
data ={
        'ph': 9.4451298379,
        'Hardness': 145.8054024468,
        'Solids': 13168.529155676,
        'Chloramines': 9.4444710856,
        'Sulfate': 310.5833738586,
        'Conductivity': 592.659020976,
        'Organic_carbon': 8.606396747,
        'Trihalomethanes': 77.5774595104,
        'Turbidity': 3.8751652466        
}

# Array de data
# data = [
#     {
#     'ph': 7.7984536762012135,
#     'Hardness': 188.39494231709176,
#     'Solids': 32704.569285770576,
#     'Chloramines': 11.078872478914501,
#     'Sulfate': 258.1911841475428,
#     'Conductivity': 507.1786882733106,
#     'Organic_carbon': 18.272439235274646,
#     'Trihalomethanes': 85.17766213336226,
#     'Turbidity': 4.107267203260775,
#     },
#     {
#         'ph': 0,
#         'Hardness': 204.890455,
#         'Solids': 20791.318981,
#         'Chloramines': 7.300212,
#         'Sulfate': 368.516441,
#         'Conductivity': 564.308654,
#         'Organic_carbon': 10.379783,
#         'Trihalomethanes': 86.990970,
#         'Turbidity': 2.963135,
#     },
#     {
#         'ph': 9.4451298379,
#         'Hardness': 145.8054024468,
#         'Solids': 13168.529155676,
#         'Chloramines': 9.4444710856,
#         'Sulfate': 310.5833738586,
#         'Conductivity': 592.659020976,
#         'Organic_carbon': 8.606396747,
#         'Trihalomethanes': 77.5774595104,
#         'Turbidity': 3.8751652466
#     }
# ]

response = requests.post(search_api_url, json=data, timeout=10)

print(response.json())