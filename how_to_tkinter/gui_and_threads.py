import tkinter as tk
import time
import queue
import concurrent.futures
import random
import threading
from queue import Queue

class ThreadedClient:

    def __init__(self, root):

        self.root = root
        self.queue = queue.Queue()
        self.running = True
        self.gui = Gui(self.root, self.queue, self.start_threads, self.stop_threads, self.quit_all)


    def start_threads(self, event):
    
        print("Starting threads")
        
        thread_names = list("ABC")

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
            executor.map(self.thread_function, thread_names, [self.queue for _ in thread_names])

        msg = "All threads are finished!" 
        print(msg)
        # self.queue.put(msg)

    def stop_threads(self):
        pass

    def quit_all(self):
        self.queue.put("QUIT")
        root.destroy()

    def thread_function(self, name: str, q: Queue):

        finish_state = 5
        state = 0

        print(f"Starting thread {name}.")
        print(f"{name}: ({state}/{finish_state}) {state < finish_state}")   
        while state < finish_state:
            sleep_time = random.random() * 2
            msg = f"Thread {name}, State == {state}, sleep: {sleep_time}"
            q.put(msg)
            time.sleep(sleep_time)
            state += 1
        print(f"Thread {name} is finished.")
        q.put("QUIT")

class Gui:

    def __init__(self, root, queue, start_threads, stop_threads, quit_all):
        
        self.queue = queue

        self.btn_start = tk.Button(root, text="Start threads")
        self.btn_stop = tk.Button(root, text="Stop threads")
        self.btn_quit = tk.Button(root, text="Quit", command=root.destroy)
        self.lbl_1 = tk.Label(root, text="1")
        self.lbl_2 = tk.Label(root, text="2")
        self.lbl_3 = tk.Label(root, text="3")

        self.btn_start.grid(column=0, row=0, rowspan=1, sticky="ns", padx=5, pady=5)
        self.btn_stop.grid(column=0, row=1, rowspan=1, sticky="ns", padx=5, pady=5)
        self.btn_quit.grid(column=0, row=2, rowspan=1, sticky="ns", padx=5, pady=5)
        
        self.lbl_1.grid(column=1, row=0, stick="nsew", padx=1, pady=1)
        self.lbl_2.grid(column=1, row=1, stick="nsew", padx=1, pady=1)
        self.lbl_3.grid(column=1, row=2, stick="nsew", padx=1, pady=1)

        self.btn_start.bind("<Button-1>", start_threads)
        self.btn_stop.bind("<Button-1>", stop_threads)
        self.btn_stop.bind("<Button-1>", quit_all)

        self.thread_incoming = threading.Thread(target=self.process_incoming, args=(None,))
        self.thread_incoming.start()

    def process_incoming(self, jalla):
        "If there's anything in the queue, handle it."
        
        while True:
            while not self.queue.empty():
                msg = self.queue.get()
                print(msg)  # Or something more clever
                if msg == "QUIT":
                    
                    return
            time.sleep(0.5)

root = tk.Tk()
client = ThreadedClient(root)
root.mainloop()
client.gui.