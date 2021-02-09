
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import pandas as pd
import numpy as np


class Toggl():

    def __init__(self):
        self.log_out_str = ""
        self.total_work_days = 0

    def log_output(self, input_str):
        self.log_out_str += input_str + "\n"

    def return_log(self):
        return self.log_out_str
    
    def welcome_msg(self):
        self.log_output("")


    # -----------------------------------------------------------
    # Print details to console GUI
    # -----------------------------------------------------------
    def print_new_day(self, day, dayIdx):
        self.log_output("----------------------------------------------------------------------------")
        self.log_output("PROJECTS WORKED ON: {}".format(day))
        self.log_output("----------------------------------------------------------------------------")
        self.log_output("TYPE\t\tPROJ ID\t\tTIME SPENT\tREC ITEM")
        self.log_output("----------------------------------------------------------------------------")
        for _, val in sap_hrs_dict.items():
            if val.__len__() < dayIdx:
                val.append(0)


    # -----------------------------------------------------------
    # Log results for GUI console
    # Store Projects, Hours, and Days in arrays
    #
    # global types, sap, time_, sap_hrs_dict
    # -----------------------------------------------------------
    def print_proj_details(self, idx, client, proj, tt, sap_map, dayIdx, new_day_flag):        
        print("Day Indx: {}, New Day: {}".format(dayIdx, new_day_flag))
        if (client + 1 < proj.size):
           print("Prev Proj: {}, Curr Proj: {}, next Proj: {}".format(proj[idx[client-1]], proj[idx[client]], proj[idx[client + 1]]))
        else: 
           print("Prev Proj: {}, Curr Proj: {}".format(proj[idx[client-1]], proj[idx[client]]))
        print("Client: {}, idx size: {}, proj size: {}".format(client, idx.size, proj.size))
        
        # TODO client-1 index will call last element in array (could lead to bug, ie last project == current proj)

        if ((client + 1 < proj.size and proj[idx[client]] != proj[idx[client + 1]]) and \
            not new_day_flag and dayIdx != 0) or \
            (client + 1 == proj.size and proj[idx[client-1]] != proj[idx[client]]):

            # current proj & hours worked
            (SAP, time_spent) = proj[idx[client]], tt   

            # verify number in hours worked
            if not np.isnan(SAP):

                # loop through all registered SAP Proj numbers               
                for k, v in sap_map.items():

                    # if matched - valid project work
                    if str(k) in str(SAP):
                        out_str = str(v) + '\t\t' + str(SAP) + '\t' + str(round(time_spent / 3600, 2))
                        self.log_output(out_str)

                        types.append(v)
                        sap.append(SAP)
                        time_.append(time_spent / 3600)

                        hrs_arr = []
                        for client_hrs in sap_hrs_dict[k]:
                            # print("Appending HRS: {} to Client: {}".format(client_hrs, sap_hrs_dict[k]))
                            hrs_arr.append(client_hrs)

                        hrs_arr.append(time_spent / 3600)
                        sap_hrs_dict[k] = hrs_arr
            return 0
        else:
            return tt

    
    # -----------------------------------------------------------
    # Read in Toggl detailed report
    # Sort by Start day & Client
    # Add hours for each project
    # -----------------------------------------------------------
    def read_data(self, filename, sap_map):
        if error:
            return
        df_sorted = (pd.read_csv(filename).rename(columns=lambda x: x.strip(","))).sort_values(
            by=['Start date', 'Client'])
        proj = df_sorted['Client']
        dur = df_sorted['Duration']
        s_date = df_sorted['Start date']
        
        # Get total number of work days (Friday bug)
        (_, _, dl) = df_sorted['Start date'].iloc[-1].split('-')
        (_, _, df) = df_sorted['Start date'].iloc[0].split('-')        
        self.total_work_days = int(dl) - int(df)
        print("Number of days worked: {}".format(self.total_work_days))

        idx = df_sorted.index
        tt = 0
        dayIdx = -1

        for client in range(df_sorted['Client'].size):
            # print("Checking client: {}, on date: {}".format(idx[client], s_date[idx[client]]))
            (h, m, s) = dur[idx[client]].split(":")

            # New day
            if s_date[idx[client]] != s_date[idx[client-1]]:
                dayIdx += 1
                self.print_new_day(s_date[idx[client]], dayIdx)
                new_day_flag = True
                tt = int(h) * 3600 + int(m) * 60 + int(s)

            # Still in same day 
            else:
                new_day_flag = False
                tt += int(h) * 3600 + int(m) * 60 + int(s)

            tt = self.print_proj_details(idx, client, proj, tt, sap_map, dayIdx, new_day_flag)


    # -----------------------------------------------------------
    # Map projects from Internal order sheet to Toggl Clients
    # -----------------------------------------------------------
    def map_projects(self, filename, sap_map):
        self.log_output("Mapping SAP from Internal Order Sheet")
        # print("Mapping SAP")
        sap_arr = []
        type_arr = []
        # rec_arr = []
        global error

        try:
            df = pd.read_csv(filename).rename(columns=lambda client: client.strip(","))
        except FileNotFoundError:
            self.log_output("-----------ERROR-----------------------------------------")
            self.log_output("Internal Order sheet not found: {}".format(filename))
            error = 1
            return

        sap_num = df['SAP_NUM']
        type = df['TYPE']
        # rec_item = df['REC_ITEM']
        for client in sap_num:
            sap_arr.append(client)
        for client in type:
            type_arr.append(client)
        # for client in rec_item:
        #     rec_arr.append(client)

        for client in range(df['SAP_NUM'].size):
            sap_map[sap_arr[client]] = type_arr[client]
            # rec_map[sap_arr[client]] = rec_arr[client]


    # ---------------------------------------------------------------------------
    # Write CSV file for CUT/PASTE into SAP
    #
    # SAP HEADERS
    # ActTyp    RecSaleOrd  RecItm  Rec.Order   Network SOp Spl A/AType WageType    AInd    M T W T F S S
    # Create SAP formatted CAT2 time sheet
    # ---------------------------------------------------------------------------
    # REC TYPE      |   REC ORDER   |       M   |   T   |   W   |   T   |   F   |
    # ---------------------------------------------------------------------------
    # 31CHTE            15010942            2.3     0       2       1       0   |
    # 31CHTE            15010950            1.0     0       4       2       0   |
    # 10LBR1            15011164            2.0     0       1       0       0   |
    # ---------------------------------------------------------------------------
    @staticmethod
    def write_sap_output(out_file, sap_map):
        with open(out_file, "w") as out:
            out.write("REC_TYPE, , , REC_ORDER,,,,,,,,,MON, TUE, WED, THUR, FRI\n")
            for k, v in sap_hrs_dict.items():
                try:
                    if k != 'TBD':
                        if type(k) == float:
                            print("Ignoring project: {}".format(str(k)))
                        else:
                            if int(k) > 10000000 and np.sum(v):
                                # CHTET FORMAT
                                print("Logging Proj: {} with {} hours".format(int(k), np.sum(v)))
                                out.write(str(sap_map[k]) + ", , ,")        # ActTyp (i.e. 31CHTE)
                                out.write(str(k) + ",,,,,,,,,")             # 15010942
                                for i in v:                                 # M T W T F
                                    out.write(str(round(i, 2)) + ", ")      # 0 1 5 0 1
                                out.write("\n")

                            if 1 < int(k) < 10000000 and np.sum(v):
                                # ORRD PROJECTS FORMAT
                                #                # ActType, RecSales, RecItm
                                out.write(str(sap_map[k]) + "," + str(k) + "," + str(rec_map[k]))
                                out.write(",,,,,,,,,,")
                                for i in v:                                 # M T W T F
                                    out.write(str(round(i, 2)) + ", ")      # 0 1 5 0 1
                                out.write("\n")

                except TypeError:
                    print("No specified SAP Project Number", k, v)


    # ---------------------------------------------------------------------------
    # Main loop called from Main GUI Class
    # ---------------------------------------------------------------------------
    def main(self, toggl_file, internal_order, output_file):
        # print("Reading toggle file: {}".format(toggl_file))
        sap_map = {}
        global types, sap, time_, week, sap_hrs_dict, error, rec_map
        types = []
        sap = []
        time_ = []
        rec_map = {}
        week = {}
        sap_hrs_dict = {}
        error = 0

        # Map SAP Number to Work Type (ie 15010942 -> 31CHTE)
        # Given my Jennifer
        self.map_projects(internal_order, sap_map)

        # add SAP Order numbers to dict
        for k, _ in sap_map.items():
            sap_hrs_dict[k] = []

        # Read and Calculate Toggl Detailed Time sheet
        # Exported by Toggle 'Detailed weekly CSV'
        self.read_data(toggl_file, sap_map)

        # Write to SAP CAT2 Format time sheet for copy and paste
        self.write_sap_output(output_file, sap_map)

