# https://realpython.com/intro-to-python-threading/

# import threading  # The basic Python threading module
import concurrent.futures  # Use ThreadPoolExecuteor instead
import random
import time

def thread_function(name: str):

    """
    The threading (target) function, of which several will run
    in parallell.
    """

    sleep_time = random.random() * 5
    print(f"Thread {name} starting. Sleep time is {sleep_time:.2f} seconds.")
    time.sleep(sleep_time)
    print(f"Thread {name} finished.")


if __name__ == "__main__":

    thread_names = list("ABCD")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(thread_names)) as executor:
        # Send content of iterable as argument(s) to the target function
        executor.map(thread_function, thread_names)

    # All the threads have to finish and join before moving on  
    print("All the threads are finished.")
  