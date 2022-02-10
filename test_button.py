
from tkinter import END

"""

De method van de testbutton en de delete button.
Ik ben nog van plan om de delete button te verhuizen naar
de numpad_class.py omdat.. ja het hoort bij numpad. :))

"""


def testbutton(voyage):
    for each_entry in voyage.data_entry_box_col:
        if len(each_entry.get()) != 0:
            print(each_entry.get())


def delete_button(root):
    entry = root.focus_get()
    entry.delete(0, END)



