import tkinter as tk
import the_threads
import concurrent.futures
from queue import Queue

# WIP... based on this:
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s07.html


class Gui():

    def __init__(self, root, queue):

        self.queue = queue

        self.btn_only = tk.Button(root, text="Click me")
        self.lbl_1 = tk.Label(root, text="1")
        self.lbl_2 = tk.Label(root, text="1")
        self.lbl_3 = tk.Label(root, text="1")

        self.btn_only.grid(column=0, row=0, rowspan=3, sticky="ns", padx=5, pady=5)
        self.lbl_1.grid(column=1, row=0, stick="nsew", padx=1, pady=1)
        self.lbl_2.grid(column=1, row=1, stick="nsew", padx=1, pady=1)
        self.lbl_3.grid(column=1, row=2, stick="nsew", padx=1, pady=1)

        self.btn_only.bind("<Button-1>", start_threads)

    def process_incoming(self):

        while self.queue.qsize():
            msg = self.queue.get(0)
            print(type(msg), msg)



class ThreadedClient(self):

    def __init__(self, root):

        self.root = root
        self.queue = Queue()
        self.gui = Gui(root, queue)       

        self.running = True
        
        # WIP....
        ## self.thread 



def thread_function(name):

    t = the_threads.SomeThread(name=name)
    t.thread_function()

def start_threads(event):
    
    thread_names = list("ABC")

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
        executor.map(thread_function, thread_names)
        
    print("All threads are finished!")


root = tk.Tk()
client = ThreadedClient(root)
root.mainloop()
