from tkinter import E, END, W, ttk
from test_button import delete_button, testbutton

"""

Door deze class te initialiseren wordt er een numpad te voorschijn getoverd.
Het numpad wordt uiteindelijk 0-9 + 4 "tekst" knoppen + een "delete" knop.
button_list is de lijst met tekst die op de knoppen moet komen.

"""
# test

class Numpad_buttons:
    def __init__(self, button_list, voyage, frame, root) -> None:
        self.button_list = button_list
        x = 1
        y = 1
        for name in self.button_list:  # voor each in de button list
            button = ttk.Button(  # komt een button
                frame,
                takefocus=False,
                text=name
            )
            button.grid(  # in een grid
                column=x,
                row=y,
                sticky=(W, E)
            )
# als er specifieke tekst gevonden wordt, wordt er specifieke command toegwzn.
            if name == "test":
                button.configure(command=lambda: testbutton(voyage))
            elif name == "Del":
                button.configure(command=lambda: delete_button(root))
            else:
                button.configure(
                    command=lambda: self.append_letter(button['text'], root))
                print(name)  # print elke letter in list in cli
            x += 1

            if x > 3:  # hier wordt er na 3 knoppen op een regel,
                y += 1  # de volgende regel toegewezen.
                x = 1

    """
    En hier onder gaat het dan fout. Daar waar de print hierboven gewoon elke
    name in de list, netjes print. Print hij hier steeds de laatste.
    Maar ik heb geen flauw idee waarom die dus (alleen) de laatste pakt.

    De method zou moeten krijgen: de "text" die op de knop weergegeven wordt,
    Root wordt doorgegeven om te zien welke textbox in focus is,
    zodat de method weet in welke textbox hij moet schrijven.
    Dit werkt (let wel op; Als er geen textbox is geselecteerd,
    geeft hij op CLI een error. Dit moet ik nog op gaan vangen op 1 of andere
    manier.)
    """
    def append_letter(self, text, root):
        print(text)  # Deze zou de text van de knop moeten weergeven.
        self.entry = root.focus_get()  # maar print altijd "test"
        self.entry.insert("end", text)  # dat is de laatste in de list.
