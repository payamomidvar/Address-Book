import tkinter as tk
from repositories import repository


class DeleteContactWindow:

    def yes(self):
        name = self.name
        repository.remove_contact(name)
        repository.commit()
        self.call_back()
        self.top.destroy()

    def no(self):
        self.call_back()
        self.top.destroy()

    def __init__(self, master, name, call_back_function):
        self.call_back = call_back_function
        top = self.top = tk.Toplevel(master)
        self.master = master
        self.name = name
        top.title('Confirm')

        self.label = tk.Label(top,
                              text='''Are you sure you want to delete this contact?''')
        self.label.grid(row=0, column=1, padx=20, pady=10)

        self.yes_button = tk.Button(top, text='Yes', command=self.yes)
        self.yes_button.grid(row=1, column=1)

        self.no_button = tk.Button(top, text='No', command=self.no)
        self.no_button.grid(row=2, column=1, pady=10)
