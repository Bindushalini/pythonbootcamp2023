import os

import requests
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

my_email = os.environ.get("FROM_EMAIL_ID")
my_pass = os.environ.get("USER_PASSWORD")

sheety_get_endpoint = os.environ.get("SHEETY_CUST_ENDP")


def get_customer_data():
    get_response = requests.get(url=sheety_get_endpoint)
    return get_response.json()['cust']

image_data = {
    "Bali": 'bali.jpg',
    "Sydney": 'sydney.jpg'
}
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
                    connect.sendmail(from_addr=from_addr, to_addrs=to_addr,
                                     msg=f"Subject: Flight deals !!Time to travel!\n"
                                         f"Hi {name}\nHurry up & head to  : {data['to']}-{data['to_code']} from : {data['from']}- {data['from_code']} with "
                                         f"lowest price of {data['price']}$ on {data['departure'][0]} at {data['departure'][1]}\n ")
                    connect.close()

    @staticmethod
    def get_message_root(user_name, data, source_addr, dest_addr):
        msg_root = MIMEMultipart()
        msg_root['Subject'] = f"Flight deals to {data['to']}!! Time to travel!\n "
        msg_root['From'] = source_addr
        msg_root['To'] = dest_addr
        image_file = image_data[data['to']]
        text = MIMEText('<img src="cid:my_images">', 'html')
        html = """\
        <html>
          <head></head>
          <body>
            <p><b>Hi $(user_name)!<br><br>
               Hurry up & head to $(to)- $(to_code) : $(from) - $(from_code): 
               with lowest price of $$(price) on $(start_date) at $(start_time) <br><br>
               Regards,<br>
               FlightNotifier<br>
            </b></p>
          </body>
        </html>
        """
        html = html.replace("$(user_name)", user_name)
        html = html.replace("$(to)", data['to'])
        html = html.replace("$(to_code)", data['to_code'])
        html = html.replace("$(from)", data['from'])
        html = html.replace("$(from_code)", data['from_code'])
        html = html.replace("$(price)", str(data['price']))
        html = html.replace("$(start_date)", str(data['departure'][0]))
        html = html.replace("$(start_time)", str(data['departure'][1]))
        body = MIMEText(html, 'html')
        msg_root.attach(text)
        msg_root.attach(body)
        img_ptr = open(image_file, 'rb').read()
        image = MIMEImage(img_ptr, os.path.basename(image_file))
        image.add_header('Content-ID', '<my_images>')
        msg_root.attach(image)
        return msg_root

    def send_mail_with_image(self, flight_data):
        os.chdir('Day22-40/CheapFLightsNotifier2/images')
        for cust in self.customer_data:
            name = cust['firstName'] + " " + cust['lastName']
            to_addr = cust['email']
            for data in flight_data:
                if data is not None:
                    from_addr = my_email
                    message = self.get_message_root(name, data, from_addr, to_addr)
                    connect = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
                    connect.login(user=from_addr, password=my_pass)
                    connect.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=message.as_string())
                    connect.close()
