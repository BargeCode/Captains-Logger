from tkinter import E, END, W, ttk
from test_button import delete_button, testbutton


class Numpad_buttons:
    def __init__(self, button_list, voyage_obj, frame, root) -> None:
        self.button_list = button_list
        x = 1
        y = 1
        for name in self.button_list:
            button = ttk.Button(
                frame,
                takefocus=False,
                text=name
            )
            button.grid(
                column=x,
                row=y,
                sticky=(W, E)
            )
            if name == "test":
                button.configure(command=lambda: testbutton(voyage_obj))
            elif name == "Del":
                button.configure(command=lambda: delete_button(root))
            else:
                button.configure(command=lambda: self.append_letter(button['text'], root))
                print(name)
            x += 1

            if x > 3:
                y += 1
                x = 1

    def append_letter(self, text, root):
        print(text)
        self.entry = root.focus_get()
        self.entry.insert("end", text)
