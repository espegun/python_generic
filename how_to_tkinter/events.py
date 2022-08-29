import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
    if event.char == "q":
        window.destroy()


def btn1_clicked(event):
    print("Button 1 clicked.")


btn_1 = tk.Button(window, text="Click me!")
btn_1.pack()

# Bind takes two arguments:
#   event - any of Tkinter's events like "<Key>", "Button"
#   event handler - the function which will be called
# Event types:
# https://python-course.eu/tkinter/events-and-binds-in-tkinter.php

# Left-click button
btn_1.bind("<Button-1>", btn1_clicked)


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()