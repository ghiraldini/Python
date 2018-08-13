#!/usr/bin/env python3

# Creating a dictionary
# A dictionary can be created by using the braces operator {key:value}. 
# You have to specify the keys and their associated values.
# Keys can be ints, floats, strings
# Note: empty dictionary can be created as D = {}.


def contact():

    # Create a dictionary of contacts; names as keys, phone numbers as values
    contacts = {"Suresh Datta": "345-555-0101", "Colette Browning": "483-555-0119", "Skey Homsi": "485-555-0195"}

    # Ask user for a name, then display the number
    name = input("Enter a name: ")

    # If name is not in the contacts dictionary, the exception message will be displayed
    try:
        number = contacts[name]
        print("Number is: {:s}".format(number))
    except KeyError as exception_object:
        print("{:s} was not found in contacts".format(name))


    # iterating using keys
    for key in contacts.keys():
        print("D[{}] = '{}'".format(key, contacts[key]))

    # iterating using values
    for value in contacts.values():
        print(value)

    # iterating using items (key:value)
    for key, value in D.items():
        print(key,':', value)


    # containment
    print( "Suresh Datta" in contacts ) # True
    print( "345-555-0101" in contacts.values ) # True

    # delete key:value
    contacts.pop('Suresh Datta')

    # Clear dictionary
    contacts.clear()

    # delete dictionary
    del(contacts)

def main():
    D = {'jason':32, 'kathryn':33, 'charlie':1.25}
    print("Charlie is {0:.3f} years old!".format(D['charlie']))






if __name__ == "__main__":
    main()
