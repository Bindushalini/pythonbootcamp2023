import requests
from datetime import datetime
import os

NUTRITION_APP_ID_ENV = os.environ.get("NUTRITION_APP_ID")
NUTRITION_APP_KEY_ENV = os.environ.get("NUTRITION_APP_KEY")
SHEETY_USERNAME_ENV = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD_ENV = os.environ.get("SHEETY_PASSWORD")
SHEETY_AUTH_HEADER_ENV = os.environ.get("SHEETY_AUTH_HEADER")
DB_ENDPOINT_ENV = os.environ.get("DB_ENDPOINT")

nutrition_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_headers = {

    'Content-Type': 'application/json',
    'x-app-id': NUTRITION_APP_ID_ENV,
    'x-app-key': NUTRITION_APP_KEY_ENV,
}
user_input = input("Whats the update for today on fitness?")
body = {
    "query": user_input
}
response = requests.post(url=nutrition_ep, json=body, headers=nutrition_headers)
response.raise_for_status()

data = response.json()
print(data)
data = data['exercises'][0]
exercise = data["name"].title()
duration = data["duration_min"]
calories = data["nf_calories"]

date = str(datetime.now().date())
time = datetime.now().time()
time = time.strftime("%H:%M:%S")
sheety_body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
sheety_auth = {
    "Authorization": SHEETY_AUTH_HEADER_ENV,
}
user_pass = (SHEETY_USERNAME_ENV, SHEETY_PASSWORD_ENV)
sheety_endpoint = DB_ENDPOINT_ENV
response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_auth, auth=user_pass)
data = response.json()
