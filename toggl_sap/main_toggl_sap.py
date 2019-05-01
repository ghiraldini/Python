
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from toggle_2_SAP import Toggl


class Application(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((1, 10), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)

        self.create_widgets()

        self.tg = Toggl

        self.df = None
        self.load = None
        self.b = None
        self.quit = None
        self.data_list = []
        self.toggl_file = "Toggl_time_entries_2019-04-08_to_2019-04-14.csv"
        self.int_order_file = "Internal_Order_Modified.csv"
        self.output_file = "SAP_INPUT_2019-04-08.csv"

    # Create initial widgets for load/quit
    def create_widgets(self):
        # Load Button
        self.load = tk.Button(self)
        self.load["text"] = "Load Data"
        self.load["command"] = self.import_data
        self.load.pack(side="top")

        # Quit
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    # resize
    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # Line 1 = Headers, strip white space
    # Line 2 = Data
    def read_data(self):
        self.df = pd.read_csv(root.filename).rename(columns=lambda x: x.strip())

    # Bring up file import dialog
    def import_data(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select toggle report",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        print("Reading toggl report...", root.filename)
        self.tg.main(root.filename, self.int_order_file, self.output_file)
        # self.read_data()

    # Create chart of data selected
    def plot_data(self, title):
        ave = np.average(self.df[title])
        ave_str = "AVE: " + str(ave)
        self.df[title].plot()
        num = 10
        plt.plot(np.convolve(self.df[title], np.ones((num,)) / num, mode='full'))
        plt.legend(str(title), loc='lower center')
        plt.title(ave_str)
        plt.show(block=True)


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
