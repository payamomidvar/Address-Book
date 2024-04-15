import sys

import tkinter as tk
from repositories import repository
from alert_window import AlertWindow
from about_window import AboutWindow  # About window
from add_contact_window import AddContactWindow
from delete_contact_window import DeleteContactWindow
from edit_contact_window import EditContactWindow


class MainWindow(object):

    def __init__(self, master):
        self.master = master
        master.title('User Address Management System')

        menu_bar = tk.Menu(self.master)
        options = tk.Menu(menu_bar, tearoff=0)
        options.add_command(label="Save", command=lambda: repository.commit())
        options.add_command(label="Quit", command=lambda: sys.exit())
        options.add_separator()
        options.add_command(label="About",
                            command=lambda: AboutWindow(self.master))
        menu_bar.add_cascade(label="File", menu=options)
        self.master.config(menu=menu_bar)

        self.sort = tk.StringVar(master)
        self.sort.set('Last Name')
        self.sort_option_menu = tk.OptionMenu(master, self.sort, 'Last Name',
                                              'Zip', command=self.search_query)
        self.sort_option_menu.grid(row=1, column=2, sticky=tk.W, padx=10)

        self.scrollbar = tk.Scrollbar(master)
        self.book_list = tk.Listbox(master, yscrollcommand=self.scrollbar.set,
                                    height=25)
        self.book_list.grid(row=2, column=2, rowspan=18, padx=15)
        self.scrollbar.config(command=self.book_list.yview)
        self.book_list.bind('<<ListboxSelect>>', self.on_select_contact)

        self.search_bar = tk.Entry(master)
        self.search_bar.grid(row=0, column=1, padx=10)
        self.search_bar.insert(0, '')
        self.search_return = \
            tk.Button(master, text='Search',
                      command=lambda: self.search_query(self.sort.get()))
        self.search_return.grid(row=0, column=0, padx=5)

        # Initialize list of contacts
        self.search_query(self.sort.get())

        self.add_button = tk.Button(master, text='Add', command=self.add_action)
        self.add_button.grid(row=14, column=0, sticky=tk.W, padx=12)

        self.delete_button = tk.Button(master, text='Delete',
                                       command=self.delete_action)
        self.delete_button.grid(row=14, column=1)

        self.edit_button = tk.Button(master, text='Edit',
                                     command=self.edit_action)
        self.edit_button.grid(row=14, column=4, padx=10, sticky=tk.E)

        self.first_name_label = tk.Label(master, text='First Name:')
        self.first_name_label.grid(row=2, column=3)
        self.first_name = tk.Entry(master)
        self.first_name.grid(row=2, column=4)

        self.last_name_label = tk.Label(master, text='Last Name:')
        self.last_name_label.grid(row=3, column=3)
        self.last_name = tk.Entry(master)
        self.last_name.grid(row=3, column=4)

        self.address1_label = tk.Label(master, text='Address 1:')
        self.address1_label.grid(row=4, column=3)
        self.address1 = tk.Entry(master)
        self.address1.grid(row=4, column=4)

        self.address2_label = tk.Label(master, text='Address 2:')
        self.address2_label.grid(row=5, column=3)
        self.address2 = tk.Entry(master)
        self.address2.grid(row=5, column=4)

        self.city_label = tk.Label(master, text='City:')
        self.city_label.grid(row=6, column=3)
        self.city = tk.Entry(master)
        self.city.grid(row=6, column=4)

        self.state_label = tk.Label(master, text='State:')
        self.state_label.grid(row=7, column=3)
        self.state = tk.Entry(master)
        self.state.grid(row=7, column=4)

        self.zip_label = tk.Label(master, text='Zip:')
        self.zip_label.grid(row=8, column=3)
        self.zip = tk.Entry(master)
        self.zip.grid(row=8, column=4)

        self.home_label = tk.Label(master, text='Home:')
        self.home_label.grid(row=9, column=3)
        self.home = tk.Entry(master)
        self.home.grid(row=9, column=4)

        self.mobile_label = tk.Label(master, text='Mobile:')
        self.mobile_label.grid(row=10, column=3)
        self.mobile = tk.Entry(master)
        self.mobile.grid(row=10, column=4)

        self.email_label = tk.Label(master, text='Email:')
        self.email_label.grid(row=11, column=3)
        self.email = tk.Entry(master)
        self.email.grid(row=11, column=4)

        self.birthday_label = tk.Label(master, text='Birthday:')
        self.birthday_label.grid(row=12, column=3)
        self.birthday = tk.Entry(master)
        self.birthday.grid(row=12, column=4)

        self.notes_label = tk.Label(master, text="Notes")
        self.notes_label.grid(row=13, column=3)
        self.notes = tk.Entry(master)
        self.notes.grid(row=13, column=4)

        self.config_state_field('readonly')

    def search_query(self, sort):
        self.book_list.delete(0, tk.END)

        for contact in repository.search(self.search_bar.get(), sort):
            self.book_list.insert(tk.END, contact[0] + " " + contact[1])

    def add_action(self):
        AddContactWindow(self.master,
                         lambda: self.search_query(self.sort.get()))

    def delete_action(self):
        try:
            name = str(self.book_list.get(self.book_list.curselection()))
            DeleteContactWindow(self.master, name,
                                lambda: self.search_query(self.sort.get()))
        except (Exception,):
            AlertWindow(self.master, "Something is wrong, try again!")

    def edit_action(self):
        try:
            name = str(self.book_list.get(self.book_list.curselection()))
            entry = []

            try:
                entry.append(name.split()[0])
            except(Exception,):
                entry.append('')

            try:
                entry.append(name.split()[1])
            except(Exception,):
                entry.append('')

            entry_id = repository.get_by_id(entry)
            EditContactWindow(self.master, name, entry_id,
                              lambda: self.search_query(self.sort.get()))

        except(Exception,):
            AlertWindow(self.master, "No entry selected")

    def config_state_field(self, state):
        self.first_name.configure(state=state)
        self.last_name.configure(state=state)
        self.address1.configure(state=state)
        self.address2.configure(state=state)
        self.city.configure(state=state)
        self.state.configure(state=state)
        self.zip.configure(state=state)
        self.home.configure(state=state)
        self.mobile.configure(state=state)
        self.email.configure(state=state)
        self.birthday.configure(state=state)
        self.notes.configure(state=state)

    def on_select_contact(self, event):
        try:
            name = str(self.book_list.get(self.book_list.curselection()))
            self.clear_entry()

            name_entry = repository.get_contact(name)

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
            self.config_state_field('readonly')

        except(Exception,):
            return

    def clear_entry(self):

        self.config_state_field('normal')
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
