# makes 3 hot flavours,
#  Espresso: 50ml water, 18g coffee. Latter: 200ml water, 24g coffee, 150ml milk. Cappuccino: 250ml water, 24g coffee,
#  100ml milk
# price: Esp - 1.5$, Latte: 2.5$, cappuccino: 3.00$
#  resources available inside the machine; 300ml water, 200ml milk, 100g coffee
#  coins: penny: 0.01$, nickel: 0.05 $, dime: 0.10$, quarter: 0.25$
#  Requirement: print the report
# 2. check if sufficient resources , report the unavailable resource.
# 3. ask the user which kind of drink.
# 4. process coins and display balance/insufficient funds.
# 5. deduct the resources if drink is made.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$",
}


def check_ingredients(user):
    check_flag = True
    for ing in user:
        if user[ing] > resource[ing]:
            print(f"Sorry there is not enough {ing}")
            check_flag = False
    return check_flag


continue_coffee = True
while continue_coffee:
    user_input = input("What is the drink you require today, espresso/latte/cappuccino? . Type report to know the"
                       " available resource")
    # TODO-1: take the input from user. handle the report scenario to display the available resource in the machine
    # TODO-2: Calculate if the resource for coffee requested is available and report if insufficient resource in machine
    if user_input == "off":
        continue_coffee = False
    elif user_input == "report":
        for key, value in resource.items():
            print(f"{key}: {value}{units[key]}")
    else:
        user_ing_value = MENU[user_input]["ingredients"]
        if check_ingredients(user_ing_value):
            # TODO -3: Take the input of coins from user. Calculate the total and report if insufficient funds,
            #  coins: penny: 0.01$, nickel: 0.05 $, dime: 0.10$, quarter: 0.25$
            total = 0.0
            print("Please insert coins")
            total += (int(input("How many dimes?")) * 0.10)
            total += (int(input("How many quarters?")) * 0.25)
            total += (int(input("How many nickels?")) * 0.15)
            total += (int(input("How many pennies?")) * 0.01)
            if total < MENU[user_input]["cost"]:
                print("Sorry not enough money for your coffee, refunding the amount")
                continue_coffee = False
            # TODO-4: Make the coffee and display balance amount if applicable.
            # TODO-5: deduct the main resource is coffee is made.
            else:
                if total > MENU[user_input]["cost"]:
                    refund_amt = round(total - MENU[user_input]["cost"], 2)
                    print(f"Here is {units['money']}{refund_amt} change")
                    for ingd in user_ing_value:
                        resource[ingd] -= user_ing_value[ingd]
                    resource["money"] += MENU[user_input]["cost"]
                    print(f"Here is your {user_input}, enjoy!")
        else:
            continue_coffee = False
