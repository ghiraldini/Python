#!/usr/bin/env python3

# more OS stuff
import os

def main():
    file_path = "/home/jason/Desktop/file.txt"
    f = open(file_path, 'w')
    f.close()

    os.listdir()
    # delete file
    os.remove(file_path)
    # delete directory
    os.rmdir()
    os.listdir()

    os.path.exists(file_path)
    os.path.isfile(file_path)

    # File Errors
    # except FileNotFoundError
    # except PermissionError

    # unexpected error/exception
    # Exception on exception_object:

    # use 'with' to open file
    # it will close file if exception is thrown 
    # and left open
    with open(file_path, 'r') as file:




if __name__ == "__main__":
    main()

