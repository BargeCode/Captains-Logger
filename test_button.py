
from tkinter import END


def testbutton(class_voyage):
    for each_entry in class_voyage.data_entry_box_col:
        if len(each_entry.get()) != 0:
            print(each_entry.get())


def delete_button(root):
    entry = root.focus_get()
    entry.delete(0, END)



