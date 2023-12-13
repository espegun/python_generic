import time
from contextlib import contextmanager

 

@contextmanager
def get_resource():

    # Code: Get some kind of resource, e.g. a connection from a 
    # database connection pool.
    print("Let's get you a resource!")

    yield "Mockup resource"  
    # Code pauses here until the external                                 # 'with' clause is finished 

    # Code: properly clean up and close down after the resource
    # has been used
    print("Cleaning up and/or returning the resource to the pool.")


with get_resource() as res:
    i = 0
    while i < 5:
        print(f"Using {res})
        time.sleep(1)
        i += 1

print("That was fun!")
