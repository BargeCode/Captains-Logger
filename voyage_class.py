from tkinter import W, E, StringVar, ttk


"""
This is the Voyage class. It gets initiated by main.py and creates
for each item in the list a label, and a textbox.
"""


class Voyage:
    def __init__(self, frame) -> None:
        self.voy_id = StringVar()
        self.voy_tonnes = StringVar()

        # The list
        self.data_label_ls = ["Voyage ID", "Tonnes", "Draught", "Water level"]

        self.data_entry_box_col = []
        x = 0
        y = 0
        for data_label in self.data_label_ls:
            if y == 2:
                x += 2
                y = 0
            ttk.Label(
                frame,
                text=data_label
            ).grid(
                column=x,
                row=y,
                sticky=(W, E)
            )
            self.entrybox = ttk.Entry(
                frame,
                width=10,
                text=data_label.lower(),
                name=data_label.lower(),
            )
            self.entrybox.grid(
                column=x + 1,
                row=y,
                sticky=(W, E)
            )
            y += 1
            self.data_entry_box_col.append(self.entrybox)
