import tkinter as tk
from repositories.repository import init
from alert_window import AlertWindow
from sys import exit


class AddBookWindow(object):

    def __init__(self, master, call_back_function):
        self.call_back = call_back_function
        self.master = master
        self.master.title('Address Books')

        self.instruction_message = tk.Label(self.master, text='Please enter the name of your new address book')
        self.instruction_message.grid(columnspan=2, pady=10)

        self.book_name_label = tk.Label(self.master, text='Address Book Name:')
        self.book_name_label.grid(row=1, padx=10)

        self.book_name = tk.Entry(self.master)
        self.book_name.grid(row=1, column=1, padx=10)

        self.cancel_button = tk.Button(self.master, text='Cancel', command=self.close_window)
        self.cancel_button.grid(row=2, column=1)

        self.ok_button = tk.Button(self.master, text='Ok', command=self.submit)
        self.ok_button.grid(row=2, column=1, sticky=tk.E, padx=10, pady=10)

    def submit(self):

        book_name = self.book_name.get()

        if len(book_name) > 1:
            init(book_name)
            root = tk.Tk()
            self.master.withdraw()
            root.protocol("WM_DELETE_WINDOW", exit)
            self.call_back(root)
            root.mainloop()
            exit()

        else:
            AlertWindow(self.master, 'An address book name is required.')

    def close_window(self):
        self.master.destroy()
