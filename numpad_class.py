
"""
Dit is een oplossing...
Weet niet of het "OOP" is. het zijn wel minder regels.
"""


from tkinter import E, END, W, ttk


class Numpad:
    def __init__(self, frame, root) -> None:
        self.button_list = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "DEL", "0", "T"
        ]
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
        button = ttk.Button(
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
    entry = root.focus_get()
    if button.cget('text') != "DEL":
        entry.insert(END, button.cget('text'))
    else:
        entry.delete(0, END)
