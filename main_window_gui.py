# class window for creating a (main window)

from tkinter import E, N, S, W, ttk, Tk
from voyage_frame import Voyage
from sector_frame import create_sectors
from numpad_frame import Numpad
from ship_frame import Ship_frame
import time


class MainWindow(Tk):
    """ A Tkinter window instance """
    def __init__(self, name) -> None:
        super().__init__(name)
        self.title(name)
        self.columnconfigure(0, weight=1, minsize=5)
        self.rowconfigure(0, weight=1, minsize=5)
        self.minsize(width=795, height=410)

        # Setting the frame for the Mw
        main_window_frame = ttk.Frame(self, padding='3 3 12 12')
        main_window_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        voyage_data_set = Voyage(main_window_frame, self)
        create_sectors(main_window_frame)
        numpad_set = Numpad(main_window_frame, self)
        ship_set = Ship_frame(main_window_frame, self)


