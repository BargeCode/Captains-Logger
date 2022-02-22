# child class of TkinterFrame

from tkinter import CENTER, N, Frame, ttk
import time


class Ship_frame:
    def __init__(self, frame, root) -> None:
        self.master_frame = frame
        self.frame = ttk.Labelframe(
            self.master_frame,
            text="Live data",
        )

        self.frame.grid(
            column=4, row=0, sticky=(N)
        )

        # Clock
        self.clock = ttk.Label(
            self.frame,
            text=self.time_string()
        )
        self.clock.grid(column=0, row=0)
        self.clock.after(1000, self.update_sec())

        self.minute = ttk.Label(
            self.frame,
            text=self.minute_string()
        )

    def update_sec(self):
        self.clock.configure(text=self.time_string())
        self.clock.after(1000, self.update_sec)

    def update_min(self):
        self.minute.configure

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def minute_string(self):
        return time.strftime('%H:%M')
