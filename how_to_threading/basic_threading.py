import threading
import time

def threading_function(name: str, sleep_time: float):

    print(f"Threading function {name} started.")
    time.sleep(sleep_time)
    print(f"Threading function {name} finished.")

if __name__ == "__main__":

    print("Single Thread")
    th1 = threading.Thread(target=threading_function, args = ("A", 2))
    th1.start()
    th1.join()  # Wait for it to finish

    print("Several Threads")
    th2 = threading.Thread(target=threading_function, args=("B", 5))
    th3 = threading.Thread(target=threading_function, args=("C", 2))
    for th in [th2, th3]:
        th.start()
    for th in [th2, th3]:
        th.join()
    print("All the threads have finished.")

    print("That was fun.")
