
# Source: https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

import sys
from platform import uname

if "WSL" in uname().release:
    print("Tkinter is not supported in WSL.")
    sys.exit(1)

try:
    import tkinter as tk
except ModuleNotFoundError:
    print("Remember, Tkinter is not installed by default for Linux.")
    print("$ sudo apt-get install python3-tk")
    sys.exit(1)

root = tk.Tk()  # All Widgets are inside a Window, the top often name root
# root.geometry("200x200")
# Widgets are normally named widgetclass_descriptive
frm_1 = tk.Frame(root, relief=tk.GROOVE)  # Frames contain other widgets
frm_2 = tk.Frame(root, relief=tk.GROOVE)  # ...but are not required
lbl_1 = tk.Label(frm_1, text="This is a label.")
btn_1 = tk.Button(frm_2, text="Click me!")
ent_1 = tk.Entry(frm_1)  # Get and modify text with .get(), .delete() and .insert()
txt_1 = tk.Text(frm_2)  # Chars .get("<line>.<char>", "<line>.<char>")

lbl_1.pack()  # Add the widget to the Window.
btn_1.pack()
ent_1.pack()
txt_1.pack()
frm_1.pack()
frm_2.pack()

root.mainloop()  # This method listens to events like clicks and keypresses

print("That was fun.")
