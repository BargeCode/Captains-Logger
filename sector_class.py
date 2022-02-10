import time
from tkinter import CENTER, N, W, E, S, StringVar, Tk, ttk


"""

Dit is de sector class. Voor elke sector (op de rivier) , kan ik dit
intialiseren en wordt er een button + label getoverd, netjes onder elkaar.

+

verschillende methods voor button_press.

"""


class Sector:
    def __init__(self, name, kmr_start, kmr_end, sector_number, frame) -> None:
        self.s_name = StringVar()
        self.s_name.set(name)  # moet stringvar zijn van Tkinter.
        self.kmr_start = kmr_start  # begin van sector (kilometer paaltje)
        self.kmr_end = kmr_end  # eind van sector (kilometer paaltje)
        self.number = sector_number  # gewoon een int voor de x pos in grid.
        self.length = self.kmr_start - self.kmr_end  # lengte van sector.
        self.start_time = None
        self.stop_time = None
        self.sector_name_lbl = ttk.Label(  # label
            frame,
            textvariable=self.s_name,
            anchor=(CENTER),
            width=20).grid(column=0, row=sector_number)
        self.button = ttk.Button(  # button
            frame,
            text="Starten",
            command=self.button_press)
        self.button.grid(column=1, row=sector_number, sticky=(W, E))

    def start_measure(self) -> None:
        self.start_time = time.time()

    def stop_measure(self) -> None:
        self.stop_time = time.time()

    def calculate_speed(self) -> None:  # method om snelheid te berekenen.
        self.time_passed = self.stop_time - self.start_time
        self.time_passed = self.time_passed / 60 / 60  # seconds to hours.
        self.sector_speed = "{:.2f}".format(self.length / self.time_passed)

    def button_press(self):  # button press voor start/stop van registratie
        if self.start_time is None:  # start registratie als waarde = none
            self.start_measure()
            self.button['text'] = "Gestart"

        elif self.start_time is not None:  # stop registratie if waarde != none
            self.stop_measure()
            self.button['text'] = "Gestopt"

            self.calculate_speed()
