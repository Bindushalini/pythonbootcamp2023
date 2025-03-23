import os
import requests

user_choice = int(input("Do u want to add customer or send notification to all users. "
                        "Type 1 to add customer and 2 to send mail").lower())

if user_choice == 1:

    print("Welcome to Shalz flight club\nOne stop place for best flight deals in your mail")
    fname = input("What is your first name?\n")
    lname = input("What is your last name?\n")
    init_email = input("What is your email?\n")
    final_email = input("Enter the email again?\n")

    if init_email == final_email:
        sheety_post_endpoint = os.environ.get("SHEETY_CUST_POST")
        sheety_body = {
            "cust": {
                "firstName": fname,
                "lastName": lname,
                "email": final_email,
            }
        }
        response = requests.post(url=sheety_post_endpoint, json=sheety_body)
        if response.status_code == 200:
            print("you are in the club!")
        else:
            print(response.json())

else:
    # This file will need to use the DataManager,FlightSearch, FlightData,
    # NotificationManager classes to achieve the program requirements.
    from data_manager import DataManager as dm
    from flight_search import FlightSearch as fs
    from notification_manager import NotificationManager as notify

    # get the data from google sheets
    google_data = dm()
    # # google_data.update_data()
    data_from_db = google_data.retrieve_data()
    #
    # #get the price details for lower cost flight details
    search = fs().get_flight_price_details(data_from_db)

    # notify to user sending an alert message

    notify_my_data = notify()
    # notify_my_data.send_mail(search)
    notify_my_data.send_mail_with_image(search)
