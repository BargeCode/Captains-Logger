# Voyage frame class

from tkinter import E, N, W, ttk


class Voyage:
    def __init__(self, frame, master) -> None:
        """ This creates the frame inside the given frame. """
        self.target_frame = frame
        self.own_frame = ttk.Labelframe(
            self.target_frame, text="Voyage details"
        )
        self.own_frame.grid(column=0, row=0, sticky=(N, W))

        self.master = master
        # The list with boxes to create:
        self.data_ls = [
            'Voyage ID',
            'Tonnes',
            'Draught',
            'Water level'
        ]

        # Collection for easy handling the entry boxes
        self.data_entrys_col = []

        # Coordinates
        x = 0
        y = 0

        for data in self.data_ls:
            # Go Textbox > Entry, 1 down, Textbox > Entry, move over.
            if y == 2:
                x += 2
                y = 0

            # The text label
            ttk.Label(
                self.own_frame,
                text=data,
                width=8,
                anchor=(E)
            ).grid(
                column=x,
                row=y,
                sticky=(W, E)
            )

            # Entrybox
            data = ttk.Entry(
                self.own_frame,
                width=8,
                text=data.lower(),
                name=data.lower()
            )
            data.grid(
                column=x + 1,
                row=y,
                sticky=(W, E)
            )

            # Append entrybox to collection
            self.data_entrys_col.append(data)

            # Up y
            y += 1
