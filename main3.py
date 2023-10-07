# day 16:
# OOP
# from turtle import Turtle, Screen
#
# t1 = Turtle()
# print(t1)
# print(t1.color("coral"))
# t1.forward(100)
# print(t1.position())
# myscr = Screen()
# print(myscr.canvheight)
# print(myscr.canvwidth)
# myscr.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])
#
# table.align = "l"
# print(table)
# coffemachine in terms of class
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
#
# coffeem = CoffeeMaker()
# moneyobj = MoneyMachine()
# continue_coffee = True
# while continue_coffee:
#     my_menu = Menu()
#     user_input = input(f"What is the drink you require today {my_menu.get_items()}. "
#     f"Type report to know the available resource")
#     if user_input == "off":
#         continue_coffee = False
#     elif user_input == "report":
#         coffeem.report()
#         moneyobj.report()
#     else:
#         my_order = my_menu.find_drink(user_input)
#         if my_order is not None:
#             if coffeem.is_resource_sufficient(my_order) and moneyobj.make_payment(my_order.cost):
#                     coffeem.make_coffee(my_order)
#             else:
#                 continue_coffee = False

#  Day 17
# creating our own classes
# class Website:  # pascal case (NewClass) #camelcase (camelCase) #snake_case
#     def __init__(self, s, name):
#         self.id = s
#         self.name = name
#         self.load = False
#
#     def display(self):
#         print(self.id, self.name)
#
#     def start_website(self):
#         self.load = True
#
#
# u1 = Website(213, "X")
# u1.display()
# u1.start_website()

