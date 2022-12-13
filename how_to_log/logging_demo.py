# https://realpython.com/python-logging/

import logging
import time
import random

LOG_NAME = "log.txt"
logging.basicConfig(level=logging.DEBUG, filename=LOG_NAME, filemode="w")


print("Work in progress...")
for _ in range(20):
    i = random.randint(0, 5)
    try: 
        10 / i
        logging.info(f"The number is {i} and all is well.")
    except ZeroDivisionError:
        logging.error(f"The number is {i} and something didn't work.")
    time.sleep(0.2)

print(f"The logs have been written to {LOG_NAME}")
print("That was fun.")

