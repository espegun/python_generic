import numpy as np
import time

class SomeThread():

    def __init__(self, name: str):

        self.name = name
        self.state = 0

    def get_state(self):

        return self.state

    def thread_function(self, finish_state=5, mean_sleep=2.0):

        """
        mean_sleep is the inverse of lambda.
        """

        while self.state < finish_state:
            sleep_time = np.random.exponential(scale=mean_sleep)
            print(f"State == {self.state}, sleep_time == {sleep_time}")
            time.sleep(sleep_time)
            self.state += 1
        print(f"Thread {self.name} is finished.")

if __name__ == "__main__":

    st = SomeThread("ABC")
    st.thread_function()
