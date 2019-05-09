
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import tkinter as tk
from tkinter import filedialog
from tkinter import Entry
from tkinter import Label

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

        self.tg = Toggl()

        self.df = None
        self.load = None
        self.b = None
        self.quit = None
        self.txt = None
        self.label = None
        self.data_list = []
        self.toggl_file = "Toggl_time_entries_2019-04-08_to_2019-04-14.csv"
        self.int_order_file = "Internal_Order_Modified.csv"
        self.output_file = "SAP_INPUT_TEST.csv"

    # Create initial widgets for load/quit
    def create_widgets(self):
        self.winfo_toplevel().title("Toggl to SAP")

        # self.label = Label(text="Output file name:", font=("Arial Bold", 12))
        # self.label.pack(side="top")
        #
        # # SAP Output file
        # self.txt = Entry(root, width=24)
        # self.txt.setvar("<Enter File Name>")
        # self.txt.pack(side="top")

        # Load Button
        self.load = tk.Button(self)
        self.load["text"] = "Load Toggl File"
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

    # Bring up file import dialog
    def import_data(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select toggle report",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        print("Reading toggl report...", root.filename)

        # TODO: Strip csv from file and add SAP.csv
        self.output_file = root.filename + "_SAP.csv"
        self.tg.main(root.filename, self.int_order_file, self.output_file)
        self.winfo_toplevel().title("File Loaded: " + root.filename)


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
