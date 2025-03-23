
import requests
api_key = "*************************"
parameters = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
data_response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data_response.raise_for_status()
weather_data_hourly_list = data_response.json()['hourly']
is_rainy_day = False
for _ in weather_data_hourly_list[:12]:
    hourly_data = _
    weather_id = hourly_data['weather'][0]['id']
    print(weather_id)
    if int(weather_id) < 700:
        # print(f"bring an umbrella, weather is {hourly_data['weather'][0]['description']}")
        is_rainy_day = True

if is_rainy_day:
#     send message using twilio
    pass

