
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import pandas as pd
import numpy as np


def print_new_day(day, dayIdx):
    print("--------------------------------------------------")
    print("PROJECTS WORKED ON: {}".format(day))
    print("--------------------------------------------------")
    for key, val in sap_hrs_dict.items():
        if val.__len__() < dayIdx:
            val.append(0)


def print_proj_details(idx, x, proj, tt, sap_map, dayIdx, new_day_flag):
    # global types, sap, time_, sap_hrs_dict
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

                    hrs_arr = []
                    for x in sap_hrs_dict[k]:
                        hrs_arr.append(x)

                    hrs_arr.append(time_spent / 3600)
                    sap_hrs_dict[k] = hrs_arr
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
    dayIdx = -1

    for x in range(df_sorted['Client'].size):
        (h, m, s) = dur[idx[x]].split(":")
        if s_date[idx[x]] != s_date[idx[x-1]]:
            dayIdx += 1
            print_new_day(s_date[idx[x]], dayIdx)
            new_day_flag = True
            tt = int(h) * 3600 + int(m) * 60 + int(s)
        else:
            new_day_flag = False
            tt += int(h) * 3600 + int(m) * 60 + int(s)

        tt = print_proj_details(idx, x, proj, tt, sap_map, dayIdx, new_day_flag)


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


# SAP HEADERS
# ActTyp    RecSaleOrd  RecItm  Rec.Order   Network SOp Spl A/AType WageType    AInd    M T W T F S S
def write_sap_output(out_file, sap_map):
    with open(out_file, "w") as out:
        for k, v in sap_hrs_dict.items():
            try:
                if len(k) > 4 and np.sum(v):
                    out.write(sap_map[str(int(k))] + ", , ,")   # 31CHTE
                    out.write(k + ",,,,,,,,,")                  # 15010942
                    for i in v:                                 # M T W T F
                        out.write(str(round(i, 2)) + ", ")      # 0 1 5 0 1
                    out.write("\n")
            except TypeError:
                print("Not a SAP Project Number")


def main(toggl_file, internal_order, output_file):
    print("Reading toggle file: {}".format(toggl_file))
    sap_map = {}
    global types, sap, time_, week, sap_hrs_dict
    types = []
    sap = []
    time_ = []
    week = {}
    sap_hrs_dict = {}
    # Map SAP Number to Work Type (ie 15010942 -> 31CHTE)
    # Given my Jennifer
    map_projects(internal_order, sap_map)

    # add SAP Order numbers to dict
    for k, v in sap_map.items():
        sap_hrs_dict[k] = []

    # Read and Calculate Toggl Detailed Time sheet
    # Exported by Toggle 'Detailed weekly CSV'
    # Write to SAP CAT2 Format time sheet for copy and paste
    read_data(toggl_file, sap_map)
    print_new_day("FRIDAY", 5)

    write_sap_output(output_file, sap_map)

# TODO: User input for files
if __name__ == "__main__":
    main("Toggl_time_entries_2019-04-08_to_2019-04-14.csv", "Internal_Order_Modified.csv", "SAP_INPUT_2019-04-08.csv")
