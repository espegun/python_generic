from threading import Thread
from queue import Queue
import time
import random


QUIT_STRING = "QUIT"

def listening_thread(queue: Queue):

    while True:
        print("Listening thread waking up...")
        while not queue.empty():
            msg = queue.get()
            print(f"Listening thread: {msg}")
            if msg == QUIT_STRING:
                return 0
        print("Listening thread sleeping...")
        time.sleep(0.5)

        
def active_thread(queue: Queue):

    i = 0
    while i < 10:
        s = "".join(random.choices(list("ABCDEFG"), k=3))
        print(f"Active thread: {s}")
        queue.put(s)
        time.sleep(random.random())
        i += 1
    queue.put(QUIT_STRING)

if __name__ == "__main__":
    q = Queue()
    th1 = Thread(target=listening_thread, args=(q,))
    th2 = Thread(target=active_thread, args=(q,))
    for th in [th1, th2]:
        th.start()
    for th in [th1, th2]:
        th.join()

    print("That was fun.")
