import random
import smtplib

#
#
my_email = ""
my_pass = ""
my_destn_email = ""
# connect = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
# # connect.starttls()
# connect.set_debuglevel(2)
# connect.login(user=my_email, password=my_pass)
# connect.sendmail(my_email, my_destn_email, msg="Subject: Test mail from python smtp module.\n\n ")
# connect.close()
quotes = []
with open("quotes.txt", 'r') as fh:
    quotes = fh.readlines()

import datetime as dt

now = dt.datetime.now()
print(now.weekday())
# date_of_birth = dt.datetime(year=1996, month=11, day=23)
# print(date_of_birth)
if now.weekday() == 4:
    connect = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
    # # connect.starttls()
    # connect.set_debuglevel(2)
    connect.login(user=my_email, password=my_pass)
    my_quote = random.choice(quotes)
    connect.sendmail(my_email, my_destn_email, msg=f"Subject: quote.\n\n {my_quote}")
    connect.close()
