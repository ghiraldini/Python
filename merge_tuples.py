#!/usr/bin/env python3

import datetime

# [ ] Complete the function `current_date` to return today's month, day, and year
# Hint: Use an appropriate function from the datetime module

def current_date():
    D = datetime.date.today()
    m = D.month
    d = D.day
    y = D.year
    return m,d,y


def get_ave(T):
    sum_ = 0
    for x in T:
        sum_ += x

    return sum_ / len(T)


def get_max(T):
    return max(T)


def main():
   
    # [ ] Write a program to compute the average of the elements in T

    T = (23, 45, 93, 59, 35, 58, 19, 3)
    print("Ave of T: {:f}".format(get_ave(T)))
    print("MAX of T: {:d}".format(get_max(T)))


    m, d, y = current_date()
    print("Today's date is: {:2d}/{:2d}/{:4d}".format(m, d, y))


    
    # [ ] Write a program to merge the content of T1 and T2 into one tuple T
    # Correct output should be T = (5, 4, 3, 9, 2, 12)
    # T = ((5, 4, 3), (9, 2, 12)) is an incorrect output

    # Hint: Use list to/from tuple conversion

    T1 = (5, 4, 3)
    T2 = (9, 2, 12)

    t1 = list(T1)
    t2 = list(T2)
   
    L = []
    for x in t1:
        L.append(x)
    for y in t2:
        L.append(y)
    
    T = tuple(L)
    # for i in T:
    #print(T)
    #print(type(T))


if __name__ == "__main__":
    main()
