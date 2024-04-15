import tkinter as tk


class AboutWindow:

    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title("About Us")

        self.label = tk.Label(top, text="Address Book Management System")
        self.label.grid(row=1, column=0, padx=10, pady=10)
