
import datetime, timedelta
from flight_data import FlightData as flights


class FlightSearch:

    def __init__(self):
        self.successful_flight_list = []

    def get_next_date(self):
        date = datetime.datetime.now()+ datetime.timedelta(days=1)
        six_month_date = datetime.datetime.now() + datetime.timedelta(days=180)
        return date, six_month_date

    def get_flight_price_details(self, sheet_vals):
        flight_objects = flights()

        for sheets in sheet_vals:
            result_data = flight_objects.get_least_price(sheets["city"], sheets["iataCode"], sheets["lowestPrice"])
            self.successful_flight_list.append(result_data)
        return self.successful_flight_list