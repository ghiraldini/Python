import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

# -------------------------------------------- #
# Runs script as Administrator
#
# Usage: python mouser.py mousemove.py
# -------------------------------------------- #

if sys.argv[-1] != ASADMIN:
	script = os.path.abspath(sys.argv[0])
	params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
	shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
	print("Running ", sys.argv[1], " as root.")
