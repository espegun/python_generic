import concurrent.futures  # Use ThreadPoolExecuteor instead
import random
import time
        

def thread_function(name: str, arg_sleep_time: float = None):

    """
    The threading (target) function, of which several will run
    in parallell.
    """

    if not arg_sleep_time:
        sleep_time = random.random() * 5
    else:
        sleep_time = arg_sleep_time
    print(f"Thread {name} starting. Sleep time is {sleep_time:.2f} seconds.")
    time.sleep(sleep_time)
    print(f"Thread {name} finished.")


if __name__ == "__main__":

    thread_names = list("ABCD")
    thread_sleep_times = [1.2, 4.1, 2.1, 3.2]  # To use this, set TWO_ARGS = True
    
    TWO_ARGS = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
        if not TWO_ARGS:
            executor.map(thread_function, thread_names)
        else:
            executor.map(thread_function, thread_names, thread_sleep_times)

    print("All the threads are finished.")
  