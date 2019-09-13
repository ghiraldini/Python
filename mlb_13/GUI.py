#!/usr/bin/python3

import os
import time
import threading
import tkinter as tk
import queue
from tkinter import filedialog, Entry, Label
from mlb_worker import MlbWorker


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

        self.load = None
        self.quit = None
        self.txt = None
        self.label = None
        self.txt2 = None
        self.label2 = None
        self.txt3 = None
        self.label3 = None

        self.text_tag = "tt"

        self.create_widgets()

        self.dir_list = []

        self.ex = MlbWorker()
        self.queue = self.ex.get_q()

    # --------------------------------------------------------------------- #
    # Create initial widgets for load/quit
    # --------------------------------------------------------------------- #
    def create_widgets(self):
        self.winfo_toplevel().title("MLB 13-RUN GAME")

        # on boot message
        msg = "Look up all games with 13 runs in score..."
        text_item = self.canvas.create_text(20, 20, anchor="nw",
                                            text=msg, tag=self.text_tag)
        self.canvas.tag_raise(text_item)

        # Load Button
        self.load = tk.Button(self)
        self.load["text"] = "GO"
        self.load["command"] = self.load_data_directory
        self.load.grid(column=0, row=0, sticky='w'+'e')

        # Quit
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)

        self.quit.grid(column=0, row=1, sticky='w'+'e')

    # --------------------------------------------------------------------- #
    # Reconfigure scroll bar to size of canvas
    # --------------------------------------------------------------------- #
    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # --------------------------------------------------------------------- #
    # This processes all incoming messages via Queue
    # Extractor thread adds messages to Queue for display on canvas in
    # this thread.
    # Update GUI, scroll bar, and scroll to bottom automatically
    # --------------------------------------------------------------------- #
    def process_incoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.put_text(msg, False)
                root.update()
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))
                self.canvas.yview_moveto(1)
            except queue.Empty:
                pass

    # --------------------------------------------------------------------- #
    # Add text to canvas
    # Append text to bottom of existing or
    # Clear text box before adding new message
    # --------------------------------------------------------------------- #
    def put_text(self, msg, clear):
        if clear:
            self.canvas.delete(self.text_tag)
            updated_msg = msg
        else:
            old_msg = self.canvas.itemcget(self.text_tag, 'text')
            self.canvas.delete(self.text_tag)
            updated_msg = old_msg + "\n" + msg

        text_item = self.canvas.create_text(20, 20, anchor="nw",
                                            text=updated_msg,
                                            tag=self.text_tag)
        self.canvas.tag_raise(text_item)

    # --------------------------------------------------------------------- #
    # Get parent directory of data set from user
    # Set path to Extractor
    # --------------------------------------------------------------------- #
    def load_data_directory(self):
        self.init_extractor()

    # --------------------------------------------------------------------- #
    # Init Extractor Thread
    # --------------------------------------------------------------------- #
    def init_extractor(self):
        extract_thread = threading.Thread(target=self.ex.do_work_mlb_stats, args=())
        extract_thread.start()
        self.update_console()

    # --------------------------------------------------------------------- #
    # Check for incoming messages via thread every 50ms
    # Extractor will signal when it is done
    # --------------------------------------------------------------------- #
    def update_console(self):
        while self.ex.needs_update():
            self.process_incoming()
            time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    # root.iconbitmap(default='favicon.ico')
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
