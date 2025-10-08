import requests

endpoint = "" # A completar

search_api_url = "http://127.0.0.1:8000/" + endpoint

data = {
    "campo_ejemplo": 1
} # A completar

response = requests.post(search_api_url, json=data, timeout=10)

print(response.json())