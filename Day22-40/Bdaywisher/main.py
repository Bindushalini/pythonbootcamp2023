#!_!_!_!_!_!_! Extra Hard Starting Project !_!_!_!_!_!_!
import datetime as dtt
import pandas
import random
import smtplib

letter_files = "letter_templates/letter_1.txt"
letter_file1 = "letter_templates/letter_2.txt"
letter_file2 = "letter_templates/letter_3.txt"
my_pass = "knwdyeiluyaeyjwh"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dtt.datetime.now()
data_frame = pandas.read_csv("birthdays.csv")
for _, x in data_frame.iterrows():
    value = x.month
    day_val = x.day
    email_addr = x.email
    if today.month == value and today.day == day_val:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        #   actual name from birthdays.csv
        letter = random.choice([letter_files, letter_file2, letter_file1])
        with open(letter, 'r') as lh:
            text = lh.readlines()
            text[0] = text[0].replace("[NAME]", x["name"])
            text = "".join(text)
            # 4. Send the letter generated in step 3 to that person's email address.
            from_addr = "bindu239681@gmail.com"
            to_addr = email_addr
            connect = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
            connect.login(user=from_addr, password=my_pass)
            # connect.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=f"Subject: happy birthday from Bindu's python "
            #                                                             f"project.\n\n{text}")
            connect.close()
