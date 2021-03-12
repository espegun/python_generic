# https://www.datacamp.com/community/tutorials/decorators-python

import time


def wrap_timer_around_this_func(func):

    def wrapper(arg1):

        t1 = time.time()
        func(arg1)
        t2 = time.time()
        print(f"That took {t2-t1} time.")

    return wrapper

@wrap_timer_around_this_func
def print_greeting(name):

    print(f"Hello, my good {name}")


print_greeting("Mr. Fuzzywig")  # Wrapper has been applied.


# Alternative to the @notation
# timed_greeting = wrap_timer_around_this_func(print_greeting)  # Alternative 1
# timed_greeting("Mr. Fuddlesworth")






