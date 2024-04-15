import sys

sys.path.insert(0, 'GUI')
import tkinter as tk

from GUI.add_book_window import AddBookWindow
from GUI.main_window import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    AddBookWindow(root, lambda r: MainWindow(r))
    root.mainloop()
