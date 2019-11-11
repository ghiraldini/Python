
# Get list of foods from user
foods = input("Enter food eaten in the last 24 hrs: ")

match1 = "dairy"
match2 = "nuts"
match3 = "seafood"
match4 = "chocolate"

# Boolean if string is in string list
b1 = match1 in foods.lower()
b2 = match2 in foods.lower()
b3 = match3 in foods.lower()
b4 = match4 in foods.lower()

# Print whether string is in foods list
# Format variable with quotes
print('It is',b1,'that','"{}"'.format(foods),'contains','"{}"'.format(match1))
print('It is',b2,'that','"{}"'.format(foods),'contains','"{}"'.format(match2))
print('It is',b3,'that','"{}"'.format(foods),'contains','"{}"'.format(match3))
print('It is',b4,'that','"{}"'.format(foods),'contains','"{}"'.format(match4))

