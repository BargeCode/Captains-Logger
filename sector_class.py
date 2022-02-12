from tkinter import CENTER, DISABLED, W, E, StringVar, ttk
import time


"""
This is the Sector class. It gets initiated by main.py and creates
the labels and button for each sector, each time it gets called.
"""


class Sector:
    def __init__(self, name, kmr_start, kmr_end, sector_number, frame) -> None:
        self.s_name = StringVar()
        self.s_name.set(name)
        self.kmr_start = kmr_start
        self.kmr_end = kmr_end
        self.number = sector_number
        self.length = self.kmr_start - self.kmr_end  # calc. sector length
        self.start_time = None
        self.stop_time = None
        self.sector_result = StringVar()
        self.sector_name_lbl = ttk.Label(  # create sector name lbl
            frame,
            textvariable=self.s_name,
            anchor=(CENTER),
            width=20).grid(
                column=0, row=sector_number)
        self.sector_result_lbl = ttk.Label(  # create sector resuls lbl
            frame,
            textvariable=self.sector_result,
            anchor=(CENTER),
            width=20
            ).grid(
                column=2, row=sector_number)
        self.button = ttk.Button(  # create sector start/stop button
            frame,
            text="Starten",
            command=self.s_button_press)
        self.button.grid(column=1, row=sector_number, sticky=(W, E))

    def start_measure(self) -> None:  # start method
        self.start_time = time.time()

    def stop_measure(self) -> None:  # stop method
        self.stop_time = time.time()

    def calculate_speed(self) -> None:  # caclulatint speed method
        self.time_passed = self.stop_time - self.start_time
        self.time_passed = self.time_passed / 60 / 60  # seconds to hours.
        self.sector_speed = "{:.2f}".format(self.length / self.time_passed)
        self.sector_result.set(self.sector_speed + " Km/h")
        self.button['state'] = DISABLED

    def s_button_press(self):  # button press for start/stop sector
        if self.start_time is None:  # if no value is found, start
            self.start_measure()
            self.button['text'] = "Gestart"

        elif self.start_time is not None:  # otherwise if value is found, stop
            self.stop_measure()
            self.button['text'] = "Gestopt"

            self.calculate_speed()
