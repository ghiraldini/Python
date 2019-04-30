
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import pandas as pd
import numpy as np


def print_new_day(day):
    print("--------------------------------------------------")
    print("PROJECTS WORKED ON: {}".format(day))
    print("--------------------------------------------------")


def print_proj_details(idx, x, proj, tt, sap_map, p):
    global types, sap, time_
    # check if we're still on the same project
    if x + 1 < proj.size and proj[idx[x]] != proj[idx[x + 1]]:
        (SAP, time_spent) = proj[idx[x]], tt
        if not np.isnan(SAP):
            for k, v in sap_map.items():
                if str(k) in str(SAP):
                    # Create SAP formatted CAT2 time sheet
                    # ---------------------------------------------------------------------------
                    # REC TYPE      |   REC ORDER   |       M   |   T   |   W   |   T   |   F   |
                    # ---------------------------------------------------------------------------
                    # 31CHTE            15010942            2.3     0       2       1       0   |
                    # 31CHTE            15010950            1.0     0       4       2       0   |
                    # 10LBR1            15011164            2.0     0       1       0       0   |
                    # ---------------------------------------------------------------------------
                    print("TYPE: {}, PROJ ID: {}, TIME SPENT: {}".format(v, SAP, time_spent / 3600))
                    types.append(v)
                    sap.append(SAP)
                    time_.append(time_spent / 3600)
        return 0
    else:
        return tt


def read_data(filename, sap_map):
    df_sorted = (pd.read_csv(filename).rename(columns=lambda x: x.strip(","))).sort_values(by=['Start date', 'Client'])
    proj = df_sorted['Client']
    dur = df_sorted['Duration']
    s_date = df_sorted['Start date']
    idx = df_sorted.index
    tt = 0
    p = 0

    for x in range(df_sorted['Client'].size):
        (h, m, s) = dur[idx[x]].split(":")
        if s_date[idx[x]] != s_date[idx[x-1]]:
            print_new_day(s_date[idx[x]])

            tt = int(h) * 3600 + int(m) * 60 + int(s)
        else:
            tt += int(h) * 3600 + int(m) * 60 + int(s)

        tt = print_proj_details(idx, x, proj, tt, sap_map, p)
        if tt == 0:
            p += 1


def map_projects(filename, sap_map):
    print("Mapping SAP")
    sap_arr = []
    type_arr = []
    df = pd.read_csv(filename).rename(columns=lambda x: x.strip(","))
    sap_num = df['SAP_NUM']
    type = df['TYPE']
    for x in sap_num:
        sap_arr.append(x)
    for x in type:
        type_arr.append(x)

    for x in range(df['SAP_NUM'].size):
        sap_map[sap_arr[x]] = type_arr[x]


def main(toggl_file, internal_order):
    print("Reading toggle file: {}".format(toggl_file))
    sap_map = {}
    global types, sap, time_, week
    types = []
    sap = []
    time_ = []
    week = {}
    # Map SAP Number to Work Type (ie 15010942 -> 31CHTE)
    # Given my Jennifer
    map_projects(internal_order, sap_map)

    # Read and Calculate Toggl Detailed Time sheet
    # Exported by Toggle 'Detailed weekly CSV'
    # Write to SAP CAT2 Format time sheet for copy and paste
    read_data(toggl_file, sap_map)

    cat2 = (types, sap, time_)
    print("")
    for i in range(cat2[0].__len__()):
        print(cat2.__getitem__(0).__getitem__(i), cat2.__getitem__(1).__getitem__(i), cat2.__getitem__(2).__getitem__(i))


if __name__ == "__main__":
    main("Toggl_time_entries_2019-04-15_to_2019-04-21.csv", "Internal_Order_Modified.csv")

# container
# cat2 = {[TYPE] , [SAP_NUMBERS], [TIME_SPENT]}
type_dict = {1:"31CHTE", 2:"31CHTE", 5:"31CHTE"}
sap_list = [1,2,1,1,5]
time_spent_list = [0,3,6,2,9]
sap_hrs_dict = {}

for k, v in type_dict.items():
    sap_hrs_dict[k] = []

idx = 0
for sap_number in sap_list:
    print(type_dict.get(sap_number), sap_number, time_spent_list[idx])
    if sap_number not in sap_hrs_dict:
        print("Project has not been charged yet - add to week charges")
        sap_hrs_dict[sap_number] = [time_spent_list[idx]]
    else:
        print("Project already has charge - add new day of charges")
        hrs_arr = []
        for x in sap_hrs_dict[sap_number]:
            hrs_arr.append(x)

        hrs_arr.append(time_spent_list[idx])
        sap_hrs_dict[sap_number] = hrs_arr

    idx += 1

print("")