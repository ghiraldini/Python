
# Script to read Toggle Detailed CSV Report and convert into SAP spread sheet
# Client = SAP Project Number

# Line 1 = Headers, strip white space, parse on comma
# Line 2 = Data

import tkinter as tk
import os
from tkinter import filedialog
from tkinter import Label

from toggle_2_SAP import Toggl


class Application(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, width=600, height=800, borderwidth=1, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw",
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
        self.display_msg = "Waiting for input..."
        self.toggl_file = "Toggl_time_entries_2019-04-08_to_2019-04-14.csv"
        self.int_order_file = "Internal_Order_Modified.csv"
        self.output_file = "SAP_INPUT_TEST.csv"

    # Create initial widgets for load/quit
    def create_widgets(self):
        self.winfo_toplevel().title("Toggl to SAP")

        # self.label = Label(self.canvas, text="Waiting to upload...")
        # self.label.pack(side="top")

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

        self.output_file, ext = os.path.splitext(root.filename)
        self.output_file += "_SAP.csv"
        print("Creating SAP file...", self.output_file)
        self.tg.main(root.filename, self.int_order_file, self.output_file)
        p = self.tg.return_log()

        text_item = self.canvas.create_text(20, 20, anchor="nw", text=p, fill="white")
        bbox = self.canvas.bbox(text_item)
        rect_item = self.canvas.create_rectangle(bbox, outline="red", fill="black")
        self.canvas.tag_raise(text_item, rect_item)

        self.winfo_toplevel().title("File Loaded: " + root.filename)


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
