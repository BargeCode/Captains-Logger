import time
from tkinter import CENTER, N, W, E, S, StringVar, Tk, ttk


"""

This is the sector class

"""


class Sector:
    def __init__(self, name, kmr_start, kmr_end, sector_number, frame) -> None:
        self.s_name = StringVar()
        self.s_name.set(name)
        self.kmr_start = kmr_start
        self.kmr_end = kmr_end
        self.number = sector_number
        self.length = self.kmr_start - self.kmr_end
        self.start_time = None
        self.stop_time = None
        self.sector_name_lbl = ttk.Label(
            frame,
            textvariable=self.s_name,
            anchor=(CENTER),
            width=20).grid(column=0, row=sector_number)
        self.button = ttk.Button(
            frame,
            text="Starten",
            command=self.button_press)
        self.button.grid(column=1, row=sector_number, sticky=(W, E))

    def start_measure(self) -> None:
        self.start_time = time.time()

    def stop_measure(self) -> None:
        self.stop_time = time.time()

    def calculate_speed(self) -> None:
        self.time_passed = self.stop_time - self.start_time
        self.time_passed = self.time_passed / 60 / 60  # seconds to hours.
        self.sector_speed = "{:.2f}".format(self.length / self.time_passed)

    def button_press(self):
        if self.start_time is None:
            self.start_measure()
            self.button['text'] = "Gestart"

        elif self.start_time is not None:
            self.stop_measure()
            self.button['text'] = "Gestopt"

            self.calculate_speed()
