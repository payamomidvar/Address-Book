import tkinter as tk
from repositories.repository import add_contact
from alert_window import AlertWindow


class AddContactWindow:
    def __init__(self, master, call_back_function):
        self.call_back = call_back_function
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title('Add Contact')

        self.first_name_label = tk.Label(top, text='First Name:')
        self.first_name_label.grid()
        self.first_name = tk.Entry(top)
        self.first_name.grid(row=0, column=1, padx=10)

        self.last_name_label = tk.Label(top, text='Last Name:')
        self.last_name_label.grid(row=1)
        self.last_name = tk.Entry(top)
        self.last_name.grid(row=1, column=1)

        self.address1_label = tk.Label(top, text='Address 1:')
        self.address1_label.grid(row=2)
        self.address1 = tk.Entry(top)
        self.address1.grid(row=2, column=1)

        self.address2_label = tk.Label(top, text='Address 2:')
        self.address2_label.grid(row=3)
        self.address2 = tk.Entry(top)
        self.address2.grid(row=3, column=1)

        self.city_label = tk.Label(top, text='City:')
        self.city_label.grid(row=4)
        self.city = tk.Entry(top)
        self.city.grid(row=4, column=1)

        self.state_label = tk.Label(top, text='State:')
        self.state_label.grid(row=5)
        self.state = tk.Entry(top)
        self.state.grid(row=5, column=1)

        self.zip_label = tk.Label(top, text='Zip:')
        self.zip_label.grid(row=6)
        self.zip = tk.Entry(top)
        self.zip.grid(row=6, column=1)

        self.home_label = tk.Label(top, text='Home Phone:')
        self.home_label.grid(row=7)
        self.home = tk.Entry(top)
        self.home.grid(row=7, column=1)

        self.mobile_label = tk.Label(top, text='Mobile Phone:')
        self.mobile_label.grid(row=8)
        self.mobile = tk.Entry(top)
        self.mobile.grid(row=8, column=1)

        self.email_label = tk.Label(top, text='Email:')
        self.email_label.grid(row=9)
        self.email = tk.Entry(top)
        self.email.grid(row=9, column=1)

        self.birthday_label = tk.Label(top, text='Birthday:')
        self.birthday_label.grid(row=10)
        self.birthday = tk.Entry(top)
        self.birthday.grid(row=10, column=1)

        self.notes_label = tk.Label(top, text="Notes")
        self.notes_label.grid(row=11)
        self.notes = tk.Entry(top)
        self.notes.grid(row=11, column=1)

        self.cancel_button = tk.Button(top, text='Cancel',
                                       command=self.close_window)
        self.cancel_button.grid(row=12, column=1)

        self.add_button = tk.Button(top, text='Add', command=self.submit)
        self.add_button.grid(row=12, column=1, padx=10, sticky=tk.E)

    def close_window(self):
        self.top.destroy()

    def submit(self):

        contact = [
            self.first_name.get(), self.last_name.get(), self.address1.get(),
            self.address2.get(),
            self.city.get(), self.state.get(), self.zip.get(), self.home.get(),
            self.mobile.get(), self.email.get(),
            self.birthday.get(), self.notes.get()
        ]

        if contact[0] != '':
            add_contact(contact)

        else:
            AlertWindow(self.master, 'A first name is required.')

        self.close_window()
        self.call_back()
