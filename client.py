import requests

BASE_URL = "http://127.0.0.1:8000/interact/"

car_search = "Quiero un Nissan 2020"
financial_search = "¿Cuánto pagaría si doy un enganche de 50,000?"
general_info_search = "¿Qué beneficios ofrece Kavak?"

response = requests.post(BASE_URL, json={"query": financial_search})

print(response.json())