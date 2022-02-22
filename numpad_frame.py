
"""
This is the Numpad and Numpad button class. It gets initiated by main.py
and creates for each item in the list a button. At the bottem you will find
the button pressed method. It checks which button is pressed. So that if you
press one of the numbers, it spits out a number and if you
press DEL, it clears the Tkinter Entry.
"""


from tkinter import DISABLED, E, END, N, NORMAL, NUMERIC, W, ttk


class Numpad:
    def __init__(self, frame, root) -> None:
        self.root_frame = frame

        self.numpad_frame = ttk.Labelframe(self.root_frame, text="Numpad")
        self.numpad_frame.grid(
            column=14, columnspan=3,
            row=0, rowspan=6,
            sticky=(N, E)
        )
        # The List
        self.button_list = [
            "ALS", "RT", "DEL",
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "B", "0", "T"
        ]
        self.special_button_list = []
        # Coordinates on grid
        x = 1
        y = 1
        for button in self.button_list:
            Numpad_button(root, self.numpad_frame, button, x, y)
            if x < 3:
                x += 1
            else:
                x = 1
                y += 1
            if not button.isnumeric() and button != 'del':
                self.special_button_list.append(button)


    def disable_special_buttons(self):
        for special_button in self.special_button_list:
            special_button['state'] = DISABLED
    
    def enable_special_buttons(self):
        for special_button in self.special_button_list:
            special_button['state'] = NORMAL


class Numpad_button:
    def __init__(self, root, button_frame, button_text, x, y) -> None:
        button_text = ttk.Button(  # creates button
            button_frame,
            takefocus=False,
            text=button_text,
            command=lambda: n_button_press(button_text, root)
        )
        button_text.grid(
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

    print(entry)
    print(button)

