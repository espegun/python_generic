# Grid is normally the preferable geometry manager.
# It works by splitting windows and (sub)Frames into rows and columns
# You can have one or several widgets for each Frame

import tkinter as tk

def press_pass(event):
    print("PASS")
    global return_code
    return_code = 0
    root.quit()
    
def press_fail(event):
    print("FAIL")
    global return_code
    return_code = 1
    root.quit()

def main(device_name: str, img_filename: str):

    global root

    root = tk.Tk()
    root.title(f"Image grab from Guppy {device_name}")
    from PIL import ImageTk, Image

    frm_top = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
    frm_bottom = tk.Frame(root, relief=tk.RAISED, borderwidth=1)

    frm_top.grid(row=0, column=0)
    frm_bottom.grid(row=1, column=0)

    img = ImageTk.PhotoImage(Image.open(img_filename).resize((800, 600)))

    lbl_img = tk.Label(frm_top, image=img)
    btn_pass = tk.Button(frm_bottom, text="PASS", width=20, height=5, background="green")
    lbl_space = tk.Label(frm_bottom, text="Does this image look acceptable?", width=100)
    btn_fail = tk.Button(frm_bottom, text="FAIL", width=20, height=5, background="red")

    lbl_img.grid(row=0, column=0)
    btn_pass.grid(row=1, column=0)
    lbl_space.grid(row=1, column=1)
    btn_fail.grid(row=1, column=2)

    btn_pass.bind("<Button-1>", press_pass)
    btn_fail.bind("<Button-1>", press_fail)

    root.mainloop()

    return return_code


if __name__ == "__main__":
    x = main("DUT 1234", "test.png")
    print(f"Return value: {x}")
    print("That was fun.")
