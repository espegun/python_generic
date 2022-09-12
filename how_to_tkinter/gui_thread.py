# import tkinter as tk
# root = tk.Tk() 

import tkinter as tk
import time
import queue
import the_threads
import concurrent.futures

class ThreadedClient:

    def __init__(self, root):

        self.root = root
        self.queue = queue.Queue()
        self.gui = Guipart(self.root, self.queue)

        self.running = True
        self.thread1 = start_threads(None)
        
        self.periodic_call()

    def periodic_call(self):

        self.gui.process_incoming()
        self.root.after(200, self.periodic_call())


def thread_function(name):

    t = the_threads.SomeThread(name=name)
    t.thread_function()

def start_threads(event):
    
    thread_names = list("ABC")

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
        executor.map(thread_function, thread_names)
        
    print("All threads are finished!")

class Guipart:

    def __init__(self, root, queue, endCommand=None):
        
        self.queue = queue

        btn_only = tk.Button(root, text="Click me")
        lbl_1 = tk.Label(root, text="1")
        lbl_2 = tk.Label(root, text="1")
        lbl_3 = tk.Label(root, text="1")

        btn_only.grid(column=0, row=0, rowspan=3, sticky="ns", padx=5, pady=5)
        lbl_1.grid(column=1, row=0, stick="nsew", padx=1, pady=1)
        lbl_2.grid(column=1, row=1, stick="nsew", padx=1, pady=1)
        lbl_3.grid(column=1, row=2, stick="nsew", padx=1, pady=1)

        btn_only.bind("<Button-1>", start_threads)

    def process_incoming(self):
        "If there's anything in the queue, handle it."

        while self.queue.qsize() > 0:
            msg = self.queue.get(0)
            print(msg)  # Or something more clever

root = tk.Tk()
client = ThreadedClient(root)
root.mainloop()

################ NOW - TRY THIS ######
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s07.html
