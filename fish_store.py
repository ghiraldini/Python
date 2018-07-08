#!/usr/bin/env python3

def get_fish():
    fish_ = input("enter fish name: ")
    return fish_.title()

def get_price():
    price_ = input("enter the fish price (no symbols): ")
    return price_

fish = get_fish()
price = get_price()
print("Fish Type: " + fish + " is $" + price)

