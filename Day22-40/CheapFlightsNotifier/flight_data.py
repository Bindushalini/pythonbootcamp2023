import os

import requests
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
FLY_FROM = "BLR"


class FlightData:
    def __init__(self):
        self.endpoint = os.environ.get("FLIGHT_CODE_ENDPOINT")
        self.search_endpoint = os.environ.get("FLIGHT_SEARCH_POINT")
        self.header = {"apikey": KIWI_API_KEY}
    def get_iata_code(self, city_name):
        params = {"term": city_name, "location_types": "airport"}
        get_reponse = requests.get(url=self.endpoint, params=params, headers=self.header)
        get_reponse = get_reponse.json()
        return get_reponse["locations"][0]["code"]

    def get_departure_time(self, time):
        date_val = time.split('T')
        return date_val

    def get_details(self, response):
        message_data = {
            'from': response["cityFrom"],
            'to': response["cityTo"],
            "from_code": response['flyFrom'],
            "to_code": response['flyTo'],
            "price": response['fare']['adults'],
            "departure": self.get_departure_time(response['local_departure'])
        }
        return message_data

    def get_least_price(self, city, code, price):
        params = {
            "fly_from": FLY_FROM,
            "fly_to": code,
            "price_to": price,
            "curr": "USD"
        }
        get_response = requests.get(url=self.search_endpoint, params=params, headers=self.header)
        get_response_value = get_response.json()
        if len(get_response_value['data']) > 0:
            return self.get_details(get_response_value['data'][0])



