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
import pandas
# with open("weather_data.csv") as weather_handle:
#     data = csv.reader(weather_handle)
#     temper = [int(x[1]) for x in data if x[1] != 'temp']
#     print(temper)

data_frame = pandas.read_csv("weather_data.csv")
# print(data_frame["temp"])

data_dict = data_frame.to_dict()
# print(data_dict)

temp = data_frame["temp"].to_list()
# print(temp)
average = sum(temp)/ len(temp)
# print(average)
# print(data_frame["temp"].mean())
# print(data_frame["temp"].max())
#
# print(data_frame.day[1])
# get data from row
# print(data_frame[data_frame.temp == data_frame.temp.max()].temp)
highest_temp = data_frame[data_frame.temp == data_frame.temp.max()].temp
# print(highest_temp)
# print(((data_frame[data_frame.temp == data_frame.temp.max()].temp)*(9/5))+32)
data_mon = data_frame[data_frame.day == "Monday"]
print(data_mon.temp[0]*(9/5)+32)

# creating a data frame
