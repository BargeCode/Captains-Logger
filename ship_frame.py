# child class of TkinterFrame

from tkinter import ANCHOR, CENTER, E, N, S, W, Frame, ttk
import time


class Ship_frame:
    def __init__(self, frame, root) -> None:
        self.master_frame = frame
        self.frame = ttk.Labelframe(
            self.master_frame,
            text="Live data",
        )
        self.frame.grid(
            column=4, columnspan=1,
            row=0, rowspan=4,
            sticky=(N)
        )

        # Clock label
        self.clock = ttk.Label(
            self.frame,
            text=self.time_string(),
            anchor=(CENTER)
        )
        self.clock.grid(column=0, row=0, sticky=(W, E))
        self.clock.after(1000, self.update_sec())

        # Speed label
        self.speed = ttk.Label(
            self.frame,
            text=self.speed_string()
        )
        self.speed.grid(column=0, row=1, sticky=(W, E))
        # self.speed.after(6000, self.update_speed)

    def update_sec(self):
        """ Updates clock label. """
        self.clock.configure(text=self.time_string())
        self.clock.after(1000, self.update_sec)

    def update_speed(self):
        """ Updates speed text label. """
        self.speed.configure(text=self.speed_string())
        self.speed.after(6000, self.update_speed)

    def time_string(self):
        return time.strftime(
            '''    Date\n%d/%m/%y\n    Time\n%H:%M:%S''')

    def speed_string(self):
        pass
        # return time.strftime('test\n%H:%M')
