# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager as dm
from flight_search import FlightSearch as fs
from notification_manager import NotificationManager as notify

# get the data from google sheets
google_data = dm()
# google_data.update_data()
data_from_db = google_data.retrieve_data()

#get the price details for lower cost flight details
search = fs().get_flight_price_details(data_from_db)

#notify to user sending an alert message

notify_my_data = notify()
notify_my_data.send_message(search)

# data_from_db = [
#                 {'city': 'Cochin ', 'iataCode': 'COK', 'lowestPrice': 32, 'id': 11}]
# get the iata codes
# flight = fd()
# print(flight.get_iata_code("Paris"))


