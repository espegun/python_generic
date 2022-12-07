# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s07.html

import tkinter as tk
import time
import threading
import random
from queue import Queue
import the_threads
import concurrent.futures

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        console = tk.Button(master, text='Done', command=endCommand)

        self.btn_threads = tk.Button(master, text="Click me")
        self.btn_end = tk.Button(master, text='Done', command=endCommand)
        self.lbl_1 = tk.Label(master, text="1")
        self.lbl_2 = tk.Label(master, text="1")
        self.lbl_3 = tk.Label(master, text="1")

        self.btn_threads.grid(column=0, row=0, rowspan=2, sticky="ns", padx=5, pady=5)
        self.btn_end.grid(column=0, row=2, rowspan=1, sticky="ns", padx=5, pady=5)
        self.lbl_1.grid(column=1, row=0, stick="nsew", padx=1, pady=1)
        self.lbl_2.grid(column=1, row=1, stick="nsew", padx=1, pady=1)
        self.lbl_3.grid(column=1, row=2, stick="nsew", padx=1, pady=1)

        self.btn_threads.bind("<Button-1>", self.start_threads)

    def start_threads(self, event):

        # event is needed also when not used

        print("Hepp!")

        thread_names = list("ABC")

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
            executor.map(self.thread_function, thread_names)
        
        print("All threads are finished!")

    def thread_function(self, name):

        t = the_threads.SomeThread(name=name)
        t.thread_function()

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                print(msg)
            except Queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master

        # Create the queue
        self.queue = Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall(  )

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(200, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following two lines with the real
            # thing.
            time.sleep(rand.random() * 1.5)
            msg = rand.random()
            self.queue.put(msg)

    def endApplication(self):
        self.running = 0

rand = random.Random()
root = tk.Tk()
client = ThreadedClient(root)
root.mainloop()