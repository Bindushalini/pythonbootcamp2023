print("Welcome to tip calculator!")
bill_amount = float(input("Whats the total amount of the bill?"))
tip_amount = int(input("what is the % of tip to be added? 10% / 12% / 15%?"))
tip_amount = (tip_amount/100)+1
number_of_customers = int(input("split among how many people?"))
split_value = (bill_amount/number_of_customers) * tip_amount
split_amount = round(split_value, 2)
split_amount = "{:.2f}".format(split_amount)
print(f"split bill amount for each of you is: ${split_amount}")



