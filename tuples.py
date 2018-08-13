#!/usr/bin/env python3

# Tuple Basics

# Split a full name into the first and last names
def split_name(name):
    names = name.split(" ")
    first_name = names[0]
    last_name = names[-1]
    # pack the variables into a tuple, then return the tuple
    return (first_name, last_name)



def main():
    # Create a homogeneous int tuple
    T_int = (10, -4, 59, 58, 23, 50)

    # Create a homogeneous string tuple
    T_string = ("word", "letter", "vowel", "spell", "book", "write", "read")

    # Create heterogeneous tuples
    T = ("Tobias", 23, 25.3, [])

    # A datetime object can be a tuple element
    from datetime import datetime
    now = datetime.today() 

    T = ((1.5,2.6), "home", now)
    
    # This is not a tuple
    T = ("switch")     
    type(T)

    # Note the comma after the string makes T a tuple
    T = ("switch",)     
    type(T)





    # List of employee names
    names_list = ["Suresh", "Colette", "Skye", "Hiroto", "Tobias", "Tamara", "Jin", "Joana", "Alton"]

    # Sort the names alphabetically
    sorted_list = sorted(names_list)

    # Convert list into tuple
    names_tuple = tuple(sorted_list)

    # List converted into a tuple
    print(type(names_tuple))

    # Print the first and last name in the tuple
    print("First name is: {:s}".format(names_tuple[0]))
    print("Last name is: {:s}".format(names_tuple[-1]))





    # Collect 3 int numbers from a user
    L = []
    for i in range(3):
        tmp = int(input("Enter an int {:d}/3: ".format(i)))
        L.append(tmp ** 2)

    # Convert the list into a tuple
    T = tuple(L)


    # Unpacking tuples () optional
    (a,b) = (2,3)
    print(a)
    print(b)

    # Slicing typle
    # You can slice a tuple using the following syntax 
    # T[initial_index:final_index]
    T = ('name', [2,4], 5.3, 19)
    S = T[1:2]
    print(S)


    # Ask user for input
    name = input("Enter your full name: ")

    # Unpack the returned tuples into first, last variables
    # looks like the function returns 2 variables
    first, last = split_name(name)

    # Unpacked variables can be used separately
    print("First name: {:s}".format(first))
    print("Last name: {:s}".format(last))


    # Containment
    T = (4, [5, 6], 'name', 3.5, True)
    print("4 contained in T?", 4 in T) # True
    print("5 not contained in T?", 5 not in T ) # True (only looks at obj)
    print("5 not contained in T?", 5 in T[1] ) # True (looks inside obj)



    # Changing one of 2 identical tuples
    T1 = (10, [2, 4], 59)
    T2 = T1

    # A change in T1 is a change in T2
    T1[1][0] = 20





if __name__ == "__main__":
    main()
