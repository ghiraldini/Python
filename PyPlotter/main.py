import tkinter as tk
from tkinter import filedialog

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.load = tk.Button(self)
        self.load["text"] = "Load Data"
        self.load["command"] = self.import_data
        self.load.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    # Line 0 = Ignore
    # Line 1 = Headers
    # Line 2 = Data
    def read_data(self):
        df = pd.read_csv(root.filename)
        df[' SpectraID'].plot()
        plt.show(block=True)


    def import_data(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        print("Reading data file...", root.filename)
        self.read_data()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
