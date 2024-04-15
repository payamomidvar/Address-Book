import tkinter as tk


class AlertWindow:

    def submit(self):
        self.top.destroy()

    def __init__(self, master, message):
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title('Oops!')

        self.label = tk.Label(top, text=message)
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.yes_button = tk.Button(top, text='Ok', command=self.submit)
        self.yes_button.grid(row=1)
