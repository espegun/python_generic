# https://www.datacamp.com/community/tutorials/decorators-python

import time


def wrap_timer_around_func(func):

    """
    The decorator function, which is passed one function and returns
    a larger function with something around the received one.
    """

    def wrapper(arg1):

        t1 = time.time()
        func(arg1)
        t2 = time.time()
        print(f"That took {t2-t1} seconds.")

    return wrapper

# Example 1 - with @ notation
@wrap_timer_around_func
def print_greeting_1(name):
    "A simple, inner function"

    print(f"Hello, my good {name}!")

print_greeting_1("Mr. Fuzzywig")  # Wrapper has been applied. With the @notation, the wrapped function has it's original name.


# Example 2 - less smooth, easier understandable
def print_greeting_2(name):
    "Another simple, inner function"

    print(f"Top of the morning to you, {name}!")

timed_greeting = wrap_timer_around_func(print_greeting_2)
timed_greeting("Frank")






