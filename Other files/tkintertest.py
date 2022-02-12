import tkinter as tk

"""

Hier doet ik niks mee, had ik van het web gekopieerd als voorbeeld.

"""


class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("Test")
        self.label = tk.Label(self.root, textvariable=self.text)

        self.button = tk.Button(self.root,
                                text="Click to change text below",
                                command=self.changeText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def changeText(self):
        self.text.set("Text updated")


app = Test()
