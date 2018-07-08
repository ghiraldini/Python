#!/usr/bin/env python3

import sys

# Final Project
# Adding Machine

def get_input():
	return input("Enter integer to add or \"Q\": ")
	

def is_quit(u_in):
	if(u_in.isalpha()):
		if(u_in == "Q" or  u_in == "q" or u_in.startswith("q") or u_in.startswith("Q")):

			return True
		else:
			return False
	else:
		pass

def is_num(u_in):
	if(u_in.isdigit()):
		return True
	else:
		return False
	

def add_to_string(tot_str, add_num):
	tot_str += "\n" + str(add_num)
	return tot_str


def add_total(tot, num):
	tot += int(num)
	return tot


def display(arg, tot, tot_str):
	if(arg == "A"):
		print("Items",tot_str)
		print("Total\n",tot)
	else:
		print("Total\n",tot)
	return

def main():
	tot = 0
	tot_str = ""
	arg = sys.argv[1]
	print("Input an integer to add to the total or \"Q\" to quit")
	
	while True:
		u_in = get_input()
	
		if( is_num( u_in ) ):
			tot_str = add_to_string(tot_str, u_in)
			tot = add_total(tot, u_in)

		elif( is_quit( u_in ) ):
			display(arg, tot, tot_str)
			break
		elif( u_in == "" ):
			pass
		else:
			print(u_in,"is invalid input")

if __name__== "__main__":
	main()
