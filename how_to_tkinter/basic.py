
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
label1 = tk.Label(root, text="This is a label.")
label1.pack()  # Add the widget to the Window.

root.mainloop()  # This method listens to events like clicks and keypresses

print("That was fun.")
