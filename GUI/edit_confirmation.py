import tkinter as tk
from repositories import repository


class EditConfirmation:

    def yes(self):
        field_list = self.field_list
        repository.edit_contact(self.entry_id, field_list)
        repository.commit()
        self.call_back()
        self.top.destroy()

    def __init__(self, master, field_list, entry_id, call_back_function):
        self.call_back = call_back_function
        top = self.top = tk.Toplevel(master)
        self.master = master
        self.field_list = field_list
        self.entry_id = entry_id
        top.title('Confirm')

        self.label = tk.Label(top,
                              text='Are you sure you want to edit this contact?')
        self.label.grid(row=0, column=1, padx=10, pady=10)

        self.yes_button = tk.Button(top, text='Yes', command=self.yes)
        self.yes_button.grid(row=1, column=1)

        self.no_button = tk.Button(top, text='No',
                                   command=lambda: self.top.destroy())
        self.no_button.grid(row=2, column=1)
