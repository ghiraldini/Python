#!/usr/bin/env python3

MIN_ORDER = 0.25
MAX_ORDER = 100.0
COST = 7.99

cheese_w = input("Enter cheese order weight (numeric value): ")

if(cheese_w.isalpha()):
	print("Please enter numeric value!")
elif(float(cheese_w) >= MAX_ORDER):
	print(cheese_w, "is more than currently available stock")
elif(float(cheese_w) <= MIN_ORDER):
	print(cheese_w, "is below minimum order amount")
else:
	print(cheese_w, "costs $" + "{0:.2f}".format(float(cheese_w) * COST))


