#!/usr/bin/env python3

import math
# sqrt, trunc, ceil, floor
import random
# randint, randrange, choice, shuffle

# Precendence
# PEMD Int-Division,Modulo AS

# Division
# 5/2 = 2.5
# 5//2 = 2 (Int division)

# Square Root
# ans = math.sqrt(25)

# Modulo
# 20 % 2 = 0

# Power
# 3 ** 2 = 9

l = [25, 34, 193, 2, 81, 26, 44]

def is_even(n):
    return (n % 2) == 0

def main():
    for x in l:
        print(is_even(x))

    print(random.randint(1,10))     # prints rand int from [1-10] inclusive
    print(random.randrange(1,11))   # prints rand int from [1-10] inclusive/exclusive
    print(random.randrange(1,11,2)) # prints rand odd ints from [1-10]

    print(random.choice(l))         # pick random number from list 'l'
    print(random.shuffle(l))        # shuffles list 'l'

    print(1 ** (2 * 3) / 4 + 5)
if __name__=="__main__":
    main()




