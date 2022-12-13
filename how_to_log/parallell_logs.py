import logging
import random
import time
import threading
class SomeKindaClass():

    def __init__(self, name):

        self.name = name
        self.logger = self._make_logger() 

    def _make_logger(self):

        # The below is extracted from 
        # https://python.plainenglish.io/python-capturing-info-logs-into-multiple-files-for-analysis-f0befdcaaa33
        logger = logging.getLogger(f"logger_{self.name}")
        logger.setLevel("DEBUG")
        handler = logging.FileHandler(f"{self.name}.log")
        formatter = logging.Formatter("%(levelname)s:%(asctime)s:%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    def some_operation(self):

        i = 0
        while i < 3:
            wait_time = random.random() * 3
            time.sleep(wait_time)
            self.logger.debug(f"{self.name} just waited {wait_time} seconds.")
            i+=1 
        
        self.logger.debug(f"{self.name} finished the operation.")



if __name__ == "__main__":
    skc_a = SomeKindaClass("A")
    skc_b = SomeKindaClass("B")
    th_a = threading.Thread(target=skc_a.some_operation)
    th_b = threading.Thread(target=skc_b.some_operation)
    threads = [th_a, th_b]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    
    print("That was fun.")
