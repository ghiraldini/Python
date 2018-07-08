#!/usr/bin/env python3

def str_analysis(u_input):
	if(u_input == ""):
		return 1
	if(u_input.isalpha()):
		print("\"" + u_input + "\" is all alphabetical characters!");
		return 0
	if(u_input.isdigit()):
		if(int(u_input) > 99):
			print(u_input, "is a big number")
			return 0
		elif(int(u_input) <= 99):
			print(u_input, "is smaller than expected.")
			return 0
	else:
		print(u_input, "thats not all alpha or all digit characters.")
		return 1


while str_analysis(input("enter word or integer: ")):
	pass

