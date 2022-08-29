# https://realpython.com/python-gui-tkinter/#the-grid-geometry-manager

# Grid is normally the preferable geometry manager.
# It works by splitting windows and (sub)Frames into rows and columns
# You can have one or several widgets for each Frame

import tkinter as tk



root = tk.Tk()


frm_left = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
frm_right = tk.Frame(root, relief=tk.RAISED, borderwidth=1)

frm_left.grid(row=0, column=0)  
frm_right.grid(row=0, column=1)   

lbl_l1 = tk.Label(frm_left, text="A")
lbl_l2 = tk.Label(frm_left, text="B")
lbl_r1 = tk.Label(frm_right, text="C")
lbl_r2 = tk.Label(frm_right, text="D")
lbl_r3 = tk.Label(frm_right, text="E")
lbl_l1.grid(row=0, column=0)
lbl_l2.grid(row=1, column=0)
lbl_r1.grid(row=0, column=0)
lbl_r2.grid(row=0, column=1)
lbl_r3.grid(row=0, column=2)

# You can have one widget within a frame (.pack())
# ..or as above, several within a frame, controlled with .grid()

# Widgets may be padded (measured in pixels)
# Internally w = widget(pad)

root.mainloop()

print("That was fun.")
