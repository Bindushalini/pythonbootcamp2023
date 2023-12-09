import os

import requests
import smtplib

my_email = os.environ.get("FROM_EMAIL_ID")
my_pass = os.environ.get("USER_PASSWORD")

sheety_get_endpoint = os.environ.get("SHEETY_CUST_ENDP")


def get_customer_data():
    get_response = requests.get(url=sheety_get_endpoint)
    return get_response.json()['cust']


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.customer_data = get_customer_data()


    def send_mail(self, flight_data):
        for cust in self.customer_data:
            name = cust['firstName'] + cust['lastName']
            to_addr = cust['email']
            for data in flight_data:
                if data is not None:
                    from_addr = my_email
                    connect = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
                    connect.login(user=from_addr, password=my_pass)
                    connect.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=f"Subject: Flight deals \n\nTime to travel!\n "
                                                                                f"Hi {name}\nHurry up & head to  : {data['to']}-{data['to_code']} from : {data['from']}- {data['from_code']} with "
                                                                                f"lowest price of {data['price']}$ on {data['departure'][0]} at {data['departure'][1]}\n ")
                    connect.close()
