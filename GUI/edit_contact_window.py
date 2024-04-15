import tkinter as tk
from repositories import repository
from edit_confirmation import EditConfirmation
from alert_window import AlertWindow


class EditContactWindow:

    def __init__(self, master, name, entry_id, call_back_function):
        self.call_back = call_back_function
        top = self.top = tk.Toplevel(master)
        self.master = master
        self.name = name
        self.entry_id = entry_id
        top.title('Edit Contact')

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

        self.clear_text_entries()
        self.grab_contact()

        self.save_button = tk.Button(top, text='Save',
                                     command=self.field_return)
        self.save_button.grid(row=12, column=1, padx=10, sticky=tk.E)

        self.cancel_button = tk.Button(top, text='Cancel',
                                       command=self.close_window)
        self.cancel_button.grid(row=12, column=1)

    def field_return(self):
        field_list = [
            self.first_name.get(), self.last_name.get(),
            self.address1.get(), self.address2.get(), self.city.get(),
            self.state.get(), self.zip.get(), self.home.get(),
            self.mobile.get(),
            self.email.get(), self.birthday.get(), self.notes.get()
        ]

        if field_list[0] != '':
            EditConfirmation(self.master, field_list, self.entry_id,
                             lambda: self.call_back())

        else:
            AlertWindow(self.master, 'A first name is required.')

        self.close_window()

    def close_window(self):
        self.top.destroy()

    def grab_contact(self):
        name_entry = repository.get_contact(self.name)

        self.first_name.insert(0, str(name_entry[0]))
        self.last_name.insert(0, str(name_entry[1]))
        self.address1.insert(0, str(name_entry[2]))
        self.address2.insert(0, str(name_entry[3]))
        self.city.insert(0, str(name_entry[4]))
        self.state.insert(0, str(name_entry[5]))
        self.zip.insert(0, str(name_entry[6]))
        self.home.insert(0, str(name_entry[7]))
        self.mobile.insert(0, str(name_entry[8]))
        self.email.insert(0, str(name_entry[9]))
        self.birthday.insert(0, str(name_entry[10]))
        self.notes.insert(0, str(name_entry[11]))

    def clear_text_entries(self):
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.address1.delete(0, tk.END)
        self.address2.delete(0, tk.END)
        self.city.delete(0, tk.END)
        self.state.delete(0, tk.END)
        self.zip.delete(0, tk.END)
        self.home.delete(0, tk.END)
        self.mobile.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.birthday.delete(0, tk.END)
        self.notes.delete(0, tk.END)
