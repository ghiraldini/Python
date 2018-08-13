#!/usr/bin/env python3

import sys
import os
# getcwd()	 working directory
# chdir()	 change directory
# 			os.chdir('..')  # back 1 directory, ../
# listdir() 	 list contents
# mkdir('new_dir')
# rmdir('del_dir')
# rename('new_name', 'old_name')

# path.abspath('leaf.txt')
# path.exists('path')
# path.isfile('path')
# path.isdir('path')


def main():
	print(sys.platform)
	print(os.getcwd())
	print(os.listdir())




if __name__ == "__main__":
	main()
