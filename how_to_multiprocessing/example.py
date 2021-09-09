from multiprocessing import Pool
import random
import time

import numpy as np

if 0:
    def print_result(sum_numbers, time_spent):
        print(f"Sum={sum_random_numbers}, time={time_spent}")

    N = 10000000

    random_numbers = [int(x) for x in np.random.randint(1, 9, N)]

    print("Method 1 - straight forward")
    t1 = time.time()
    sum_random_numbers = sum(random_numbers)
    t2 = time.time()
    print_result(sum_random_numbers, t2-t1)

    print("Method 2 - Mutliprocessing on several cores")
    t1 = time.time()
    sums = []
    with Pool(2) as p:
        print(p.map(sum, random_numbers))
        # sums.append(p.map(sum, random_numbers))
    #sum_random_numbers = sum(sums)
    t2 = time.time()
    #print_result(sum_random_numbers, t2-t1)











if 1:

    from multiprocessing import Pool

    def f(x):
        return x*x

    if __name__ == '__main__':
        with Pool(5) as p:
            print(p.map(f, [1, 2, 3]))