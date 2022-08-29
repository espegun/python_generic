import tkinter as tk
import the_threads
import concurrent.futures

def thread_function(name):

    t = the_threads.SomeThread(name=name)
    t.thread_function()

def start_threads(event):
    
    thread_names = list("ABC")

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
        executor.map(thread_function, thread_names)
        
    print("All threads are finished!")


root = tk.Tk()

btn_only = tk.Button(root, text="Click me")
lbl_1 = tk.Label(root, text="1")
lbl_2 = tk.Label(root, text="1")
lbl_3 = tk.Label(root, text="1")

btn_only.grid(column=0, row=0, rowspan=3, sticky="ns", padx=5, pady=5)
lbl_1.grid(column=1, row=0, stick="nsew", padx=1, pady=1)
lbl_2.grid(column=1, row=1, stick="nsew", padx=1, pady=1)
lbl_3.grid(column=1, row=2, stick="nsew", padx=1, pady=1)

btn_only.bind("<Button-1>", start_threads)

tk.mainloop()

################ NOW - TRY THIS ######
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s07.html
