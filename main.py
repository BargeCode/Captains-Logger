from tkinter import N, W, E, S, Tk, ttk
from sector_class import Sector
from voyage_class import Voyage
from numpad_class import Numpad_buttons
from test_button import testbutton


root = Tk()  # initieerd het venster.
root.title("Captains-logger")
root.columnconfigure(0, weight=1, minsize=5)
root.rowconfigure(0, weight=1, minsize=5)

"""
hier onder wordt een raster gevormd. waarop alle 
objecten geplaatst worden a.d.v. rows en columns
"""
mainwindow_frame = ttk.Frame(root, padding="3 3 12 12")
mainwindow_frame.grid(column=0, row=0, sticky=(N, W, E, S))

voyage_frame = ttk.Labelframe(mainwindow_frame, text="Voyage control")
voyage_frame.grid(column=1, row=0, rowspan=2, sticky=(N, W))

voyage = Voyage(voyage_frame)  # hier wordt het voyage gedeelte init.

numpad_frame = ttk.Labelframe(mainwindow_frame, text="Toetsen")
numpad_frame.grid(
    column=3, columnspan=3,
    row=0, rowspan=6,
    sticky=(N, E)
    )

button_list = ["A", "B", "C", "D", "Del", "test"]  # de lijst voor de knoppen

numpad = Numpad_buttons(button_list, voyage, numpad_frame, root)  # init

sector_frame = ttk.Labelframe(mainwindow_frame, text="Sector control")
sector_frame.grid(column=1, row=3, rowspan=3, sticky=(S, W))

sector_1 = Sector("Sector A", 200, 100, 1, sector_frame)  # init sector A
sector_2 = Sector("Sector B", 100, 50, 2, sector_frame)  # init sector B
sector_3 = Sector("Sector C", 10, 5, 3, sector_frame)  # enz. enz.

# Test button gemaakt om te printen op CLI
test123button = ttk.Button(
    mainwindow_frame,
    text="test",
    command=lambda: testbutton(voyage)
    )
test123button.grid(
        column=10, row=10
    )


root.mainloop()
