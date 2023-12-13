import time

def my_yielding_function(max_int: int=5):

    i = 0
    while i <= max_int:
        print("Yielding function: Ok, let's yield a number!")
        yield i  # Pauses here until the next iteration
        i += 1
        
    print("Yielding function: The end of the function is reached.")

for number in my_yielding_function():
    print(f"Outer code: The number received: {number}")
    time.sleep(1)

print("That was fun!")
