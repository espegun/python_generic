import threading 
import time
import random

class MyOngoingProcess:

    def __init__(self):

        self.state = 0
        self.running = False

    def get_running(self):

        return self.running
    
    def get_state(self):

        return self.state

    def start_process(self):

        self.running = True

        MAX = 10
        while self.state < MAX:
            time.sleep(0.1)
            if random.random() < 0.5:
                self.state += 1
                #print(self.state)
    
        self.running = False
        self.state = 0


if __name__ == "__main__":

    mop = MyOngoingProcess()
    th = threading.Thread(target=mop.start_process)
    th.start()

    while mop.get_running():
        time.sleep(0.5)
        print(f"The process: {mop.get_running()} and state={mop.get_state()}")

    th.join()

    print("That was fun!")

