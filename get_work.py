#!/usr/bin/env python3

import os
import subprocess
import shlex
import pexpect
import re

# Get total number of commits (per specific branch)
# git shortlog -s -n --no-merges --after="2018-06-01" --author="Jason"
# 	>>> 11 Jason


def run_command(date):
    cmd = "git shortlog -s -n --after=" + date + "--author=\"Jason\""
    child = pexpect.spawn(cmd)
    #    b'\x1b[?1h\x1b=\r    10  Jason\x1b[m\r\n\r\x1b[K\x1b[?1l\x1b>'
    out = str(child.read())
    sub = re.split('\s', out)
    # print(sub)
    try:
        if sub[4].isdigit():
            hrs = sub[4]
        else:
            hrs = sub[5]

    except IndexError:
        print("No Hours worked on this branch...")
        hrs = 0

    return hrs
 

def update_hrs(commit_list, name, hrs):
    commit_list.append([name, hrs])


def calc_percent(total, commit_list):
    for (name, hrs) in commit_list:
        try:
            perc = int(hrs)/total * 100
        except ValueError:
            perc = 0
        print(name, "\t\tpercentage: {0:.2f}" .format(perc))
    
    return


def main():
    # Get all commits since this date to today
    last_month = "2019-01-01"
    total = 0
    # path of repo and branch pair
    repos = [("/home/lgr/git/icos", "950_MASTER"),
             ("/home/lgr/git/icos", "927_MASTER"),
             ("/home/lgr/git/icos", "MASTER"),
             ("/home/lgr/git/icos", "NGICOS"),
             ("/home/lgr/git/icos", "chemo_mbc"),
             ("/home/lgr/git/icos", "gga_nh3_fix"),             
             ("/home/lgr/git/icos", "chemo_mbc"),
             ("/home/lgr/git/icos", "launcher_loop"),             
             ("/home/lgr/git/icos_qt", "950_MASTER"),
             ("/home/lgr/git/icos_qt", "set_zero"),
             ("/home/lgr/git/icos_qt", "SimplifiedUI_modbus"),
             ("/home/lgr/git/icos_qt", "MEA"),
             ("/home/lgr/git/icos_qt", "gga-er-serial"),
             ("/home/lgr/git/icos_qt", "c5"),             
             ("/home/lgr/git/icos_qt_lwia", "lwia_QCharts"),
             ("/home/lgr/git/icos_qt_lwia", "master"),
             ("/home/lgr/git/icos_qt_lwia", "lc_pal_serial"),             
             ("/home/lgr/git/experimental", "master"),
             ("/home/lgr/git/experimental", "lcp_daq_qt"),             
             ("/home/lgr/git/experimental_icos", "master"),
             ("/home/lgr/git/experimental_icos", "lcp"),             
             ("/home/lgr/git/experimental_icos", "STL_DAQ")]

    commit_list = []
    log_file = "/home/lgr/monthly_commits/" + last_month + "_log.csv"

    for (path, branch) in repos:
        # Change directory
        os.chdir(path)

        # Checkout branch (git checkout <branch>)
        os.system("git checkout -f " + branch)
        branch_hrs = run_command(last_month)
        print("Branch: " + branch + ", Commits: " + str(branch_hrs))
        print()
        update_hrs(commit_list, path+"_"+branch, branch_hrs)
        try:
            total += int(branch_hrs)
        except ValueError:
            print("Error - Ignored branch hours!")
            branch_hrs = 0
            total += int(branch_hrs)
        
        os.system("echo " + branch.upper() + " WORK >> " + log_file)

        # git log --after=2018-05-21 --author="Jason" --pretty=format:"%h","%an","%ad","%s" >> log.csv
        os.system("git log --after=" + last_month + " --author=\"Jason\" --pretty=format:\"%h\",\"%an\",\"%ad\",\"%s\" >> " + log_file)
        os.system("echo \" \" >> " + log_file)
        os.system("echo \" \" >> " + log_file)

    calc_percent(total, commit_list)
    # print("Total commits: " + str(total))
    # print(commit_list)


if __name__ == "__main__":
    main()
