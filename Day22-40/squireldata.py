import pandas

squirel_df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231022.csv")
value_count = squirel_df.value_counts("Primary Fur Color").to_dict()
new_data_frame = pandas.DataFrame(value_count, index=[0])
new_data_frame.to_csv("Fur_data.csv")

# Gray," "Cinnamon" or "Black."

# squirel_color_gray = squirel_df[squirel_df["Primary Fur Color"] == "Gray"]
# print(len(squirel_color_gray))
#
# squirel_color_Cinnamon = squirel_df[squirel_df["Primary Fur Color"] == "Cinnamon"]
# print(len(squirel_color_Cinnamon))
# squirel_color_black = squirel_df[squirel_df["Primary Fur Color"] == "Black"]
# print(len(squirel_color_black))

# print(squirel_df.value_counts("Primary Fur Color"))
