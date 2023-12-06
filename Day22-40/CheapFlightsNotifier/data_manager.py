import requests, os
from flight_data import FlightData as flightd

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = []
        self.sheety_endpoint = os.environ.get("SHEETY_ENDP")

    def retrieve_data(self):
        response = requests.get(url=self.sheety_endpoint)
        self.data = response.json()
        self.data = self.data["prices"]
        return self.data

    def update_data(self):
        if len(self.data) == 0:
            self.retrieve_data()
        for row in self.data:
            if row["iataCode"] == "":
                row_id = row["id"]
                iata_code = flightd().get_iata_code(row["city"])
                sheety_body = {
                    "price": {
                        "iataCode": iata_code,
                    }
                }
                sheety_endpoint = self.sheety_endpoint + "/" + str(row_id)
                put_response = requests.put(url=sheety_endpoint, json=sheety_body)
                # print(put_response.json())
