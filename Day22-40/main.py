# Day 22

# pin pong game
# 1. 2 players moving at the side of screen
# 2. midline
# 3. ball moving diagonally across the screen
# 4. bounce back
# 5. detect collision
# 6. update score, reduce / increase the score
#
#
#  Day 23: Turtle capstone project

# 1. create a turtle and navigate it using up keypress.
# 2. create a car manager to create cars at required position, size, and move
# 3. detect collision and level up conditions
# 4. display the score / game over sequence

# Day24:
# updates to snake game
# files
# customising names in same files to multiple people

# with open("my_text.txt") as fh:
#     stri = fh.read()
# #     print(stri)
# with open("my_text.txt", "a") as fh:
#     new_text = "adding text"
#     fh.write(new_text)

# day25: csv, pandas
# guess and learn all the state of US
#  days of the week and temperature of that day
# with open("weather_data.csv") as weather_handle:
#     data = weather_handle.readlines()
#     print(data)
# import csv
# import pandas
# # with open("weather_data.csv") as weather_handle:
# #     data = csv.reader(weather_handle)
# #     temper = [int(x[1]) for x in data if x[1] != 'temp']
# #     print(temper)
#
# data_frame = pandas.read_csv("weather_data.csv")
# # print(data_frame["temp"])
#
# data_dict = data_frame.to_dict()
# # print(data_dict)
#
# temp = data_frame["temp"].to_list()
# # print(temp)
# average = sum(temp)/ len(temp)
# # print(average)
# # print(data_frame["temp"].mean())
# # print(data_frame["temp"].max())
# #
# # print(data_frame.day[1])
# # get data from row
# # print(data_frame[data_frame.temp == data_frame.temp.max()].temp)
# highest_temp = data_frame[data_frame.temp == data_frame.temp.max()].temp
# # print(highest_temp)
# # print(((data_frame[data_frame.temp == data_frame.temp.max()].temp)*(9/5))+32)
# data_mon = data_frame[data_frame.day == "Monday"]
# print(data_mon.temp[0]*(9/5)+32)

# creating a data frame

# Day 26:
# spell out the name from nato phonetic alphabets

# print([i * 2 for i in range(1, 5)])
# import random
#
# names = ["saa", "paa", "laa"]
# score = {item: random.randint(1, 100) for item in names}
#
# high_score = {item: value for item, value in score.items() if value > 65}
# print(high_score.keys())
# print(score)
#
# sentence = input()
#
# list_of_words = sentence.split(" ")
# my_dict = {words: len(words) for words in list_of_words}
# print(my_dict)
#
# weather_c = eval(input())
# faren = {key:((value * 9/5) + 32) for key,value in weather_c.items()}
# print(faren)

# looping over pandas dataframe
# for key, value in data_frame.items():
#     print(key)
#     print(value)
#
# # ==> loop through iter rows
# for index,rows in data_frame.iterrows():
#     print(index, rows)
#     print(rows.student)
#     print(rows.score)
#
# Day 27: GUI and function arguments
# unit converter program

# import tkinter
#
#
# def button_click():
#     # my_label.config(text="button got clicked")
#     my_label.config(text=input.get())
#
#
# window = tkinter.Tk()
# window.title("my gui")
# window.minsize(500, 500)
#
# my_label = tkinter.Label(text="I am a label")
# my_label.pack(side="top")
#
# button = tkinter.Button(text="click me", command=button_click)
#
# button.pack()
# # entry class
#
# input = tkinter.Entry(width=15)
# input.pack()
#
# window.mainloop()

# day 29: Building a password manager
# store and generate passwords
# ask for password input to user or generate new password.
# after adding store in a text file
#  validation
# pw generated is copied to clipboard for further usage
# 3 col X 5 row layout

# Day 30:
# try:
#     fh = open("a.txt")
#     print("x")
# except FileNotFoundError as e:
#     # except:
#     fh = open("a.txt", 'w')
#     print("creating file")
# else:
#     print(fh.read())
# finally:
#     raise KeyError("Made up")

# height = float(input("h"))
# weight = float(input("w"))
#
# if height > 3:
#     raise ValueError("height is invalid input. Should be below 3 meters")
# bmi = weight / height ** 2
# print(bmi)

# Day 31: good project to indepth about pandas and tkinter (Flashcard)
# https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html
# https://www.plus2net.com/python/tkinter-button.php#colourful

#  Day32: automated bday wisher
# email smtp - smtplib module, simple mail transfer protocol.

# tls - transport layer secuirty - avoids interception of mails by unknown
# knwd yeil uyae yjwh
# wpyo xukb ecyk ajbj

# monday motivational quotes via email

# 2 new lines separator between subject and body of mail
# dat e time -

# Day 33: API's

import requests
import datetime

#
# resp = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(resp.raise_for_status())
#
# data = resp.json()['iss_position']['latitude']
# # data = resp.json()
# print(data)
# params = {
#     "lat": 12.971599,
#     "lng": 77.594566
# }
# resp1 = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
# resp1.raise_for_status()
# data = resp1.json()
# print(data)
# sunr = int(data["results"]["sunrise"].split(":")[0])
# suns = int(data["results"]["sunset"].split(":")[0])
#
# now = datetime.datetime.now()
# print(now.hour)
#
# day 35
# twilio API is used to send text messages

#day 36
# stock trading news alert
# 1. monitoring stock price - difference between closing price of 2 days (increase or decrease) , percentage of rise/fall
# 2. if so, fetch the news related to stock.
# 3. sends a sms about the fall/rise and news info

#Day 37: HTPP requests: post, put, delete
# get - request from external system and receive the response
#post: give the data to external system and not await response .(post the data into spreadsheet / send data to twitter)
#put: update data in system
#delete: external service data delete

# pixela key: user specific
