#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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

        self.df = None
        self.load = None
        self.b = None
        self.quit = None
        self.data_list = []

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
        i = 0
        for h, d in self.df.items():
            self.b = tk.Button(self.frame, text=h, width=16, borderwidth="1", relief="solid",
                               command=lambda title=h: self.plot_data(title)).grid(row=i, column=0)
            i += 1

    # Bring up file import dialog
    def import_data(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        print("Reading data file...", root.filename)
        self.read_data()

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
