
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import pandas as pd
import numpy as np


class Toggl():

    def __init__(self):
        self.log_out_str = ""
        # self.welcome_msg()

    def log_output(self, input_str):
        self.log_out_str += input_str + "\n"

    def return_log(self):
        return self.log_out_str

    # @staticmethod
    def welcome_msg(self):
        self.log_output("")

    # @staticmethod
    def print_new_day(self, day, dayIdx):
        self.log_output("--------------------------------------------------")
        self.log_output("PROJECTS WORKED ON: {}".format(day))
        self.log_output("--------------------------------------------------")
        # print("--------------------------------------------------")
        # print("PROJECTS WORKED ON: {}".format(day))
        # print("--------------------------------------------------")
        for key, val in sap_hrs_dict.items():
            if val.__len__() < dayIdx:
                val.append(0)

    # @staticmethod
    def print_proj_details(self, idx, x, proj, tt, sap_map, dayIdx, new_day_flag):
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
                        # print("TYPE: {}, PROJ ID: {}, TIME SPENT: {}".format(v, SAP, time_spent / 3600))
                        self.log_output("TYPE: {}, PROJ ID: {}, TIME SPENT: {}".format(v, SAP, time_spent / 3600))
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

    # @staticmethod
    def read_data(self, filename, sap_map):
        if error:
            return
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
                self.print_new_day(s_date[idx[x]], dayIdx)
                new_day_flag = True
                tt = int(h) * 3600 + int(m) * 60 + int(s)
            else:
                new_day_flag = False
                tt += int(h) * 3600 + int(m) * 60 + int(s)

            tt = self.print_proj_details(idx, x, proj, tt, sap_map, dayIdx, new_day_flag)

    # @staticmethod
    def map_projects(self, filename, sap_map):
        self.log_output("Mapping SAP from Internal Order Sheet")
        # print("Mapping SAP")
        sap_arr = []
        type_arr = []
        global error

        try:
            df = pd.read_csv(filename).rename(columns=lambda x: x.strip(","))
        except FileNotFoundError:
            self.log_output("-----------ERROR-----------------------------------------")
            self.log_output("Internal Order sheet not found: {}".format(filename))
            error = 1
            return

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
    @staticmethod
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
                    print("No specified SAP Project Number")

    # @staticmethod
    def main(self, toggl_file, internal_order, output_file):
        # print("Reading toggle file: {}".format(toggl_file))
        sap_map = {}
        global types, sap, time_, week, sap_hrs_dict, error
        types = []
        sap = []
        time_ = []
        week = {}
        sap_hrs_dict = {}
        error = 0

        # Map SAP Number to Work Type (ie 15010942 -> 31CHTE)
        # Given my Jennifer
        self.map_projects(internal_order, sap_map)

        # add SAP Order numbers to dict
        for k, v in sap_map.items():
            sap_hrs_dict[k] = []

        # Read and Calculate Toggl Detailed Time sheet
        # Exported by Toggle 'Detailed weekly CSV'
        # Write to SAP CAT2 Format time sheet for copy and paste
        self.read_data(toggl_file, sap_map)
        # self.print_new_day("FRIDAY", 5)

        self.write_sap_output(output_file, sap_map)
