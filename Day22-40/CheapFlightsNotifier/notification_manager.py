import os

from twilio.rest import Client
sms_sid = os.environ.get("SMS_SID")
sms_token = os.environ.get("SMS_TOKEN")
from_number = os.environ.get("FROM_NUMBER")
to_number = os.environ.get("TO_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_message(self, flight_data):
        for data in flight_data:
            if data is not None:
                client = Client(sms_sid, sms_token)
                message = client.messages \
                    .create(body=f"\nTime to travel!\n Hurry up & head to  : {data['to']}-{data['to_code']} from : {data['from']}-"
                                 f"{data['from_code']} with lowest price of {data['price']}$ on {data['departure'][0]}"
                                 f" at {data['departure'][1]}\n ",
                            from_=from_number,
                            to=to_number)
                print(message.sid)
