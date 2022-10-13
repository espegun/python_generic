import threading
import time
import random


class CanStoreResults:

    def __init__(self):

        self.result = None

    def func_with_result(self):

        time.sleep(random.random())
        self.result = "".join(random.choices(list("ABCDEF"), k=3)) 
        return self.result  # <-- This won't go anywhere 

def threading_function(name: str, sleep_time: float):

    print(f"Threading function {name} started.")
    time.sleep(sleep_time)
    print(f"Threading function {name} finished.")

if __name__ == "__main__":

    print("Single Thread")
    th1 = threading.Thread(target=threading_function, args = ("A", 2))
    th1.start()
    th1.join()  # Wait for it to finish

    print("================")

    print("Several Threads")
    th2 = threading.Thread(target=threading_function, args=("B", 5))
    th3 = threading.Thread(target=threading_function, args=("C", 2))
    for th in [th2, th3]:
        th.start()
    for th in [th2, th3]:
        th.join()
    print("All the threads have finished.")

    print("================")

    print("Several threads with result, need to save the result to something, not return it.")
   
    CSR = [CanStoreResults(), CanStoreResults()]
    th4 = threading.Thread(target=CSR[0].func_with_result)
    th5 = threading.Thread(target=CSR[1].func_with_result)
    for th in [th4, th5]:
        print(th.start())
    for th in [th4, th5]:
        print(th.join())

    for csr in CSR:
        print(csr.result)

    print("That was fun.")
