
"""
This is the Numpad and Numpad button class. It gets initiated by main.py
and creates for each item in the list a button. At the bottem you will find
the button pressed method. It checks which button is pressed. So that if you
press one of the numbers, it spits out a number and if you
press DEL, it clears the Tkinter Entry.
"""


from tkinter import E, END, W, ttk


class Numpad:
    def __init__(self, frame, root) -> None:

        # The List
        self.button_list = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "DEL", "0", "T"
        ]

        # Coordinates on grid
        x = 1
        y = 1
        for button in self.button_list:
            Numpad_button(root, frame, button, x, y)
            if x < 3:
                x += 1
            else:
                x = 1
                y += 1


class Numpad_button:
    def __init__(self, root, frame, button_text, x, y) -> None:
        button = ttk.Button(  # creates button
            frame,
            takefocus=False,
            text=button_text,
            command=lambda: n_button_press(button, root)
        )
        button.grid(
            column=x,
            row=y,
            sticky=(W, E)
        )


def n_button_press(button, root):
    entry = root.focus_get()  # gets last active object.
    if button.cget('text') != "DEL":  # if b_text isn't del.
        entry.insert(END, button.cget('text'))  # insert b_text
    else:
        entry.delete(0, END)  # Else del.
