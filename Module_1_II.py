#!/usr/env/python3


def main():
    after_g()


# Print words that begin after letter "G"/"g" in upper case
def after_g():
    ret = ""
    flag = False
    s = input("enter a 1 sentence quote, non-alpha separate words:")
    for word in s.split(" "):
        if word[0].lower() > 'g':
            flag = True
            for l in word:
                if l.isalpha():
                    ret += l.upper()
        if flag:
            print(ret)
            ret = ""
            flag = False


if __name__ == "__main__":
    main()
