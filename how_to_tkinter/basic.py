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

window = tk.Tk()  # All Widgets are inside a Window
label1 = tk.Label(text="This is a label.")
label1.pack()  # Add Adding the widget to the Window.

print("That was fun.")