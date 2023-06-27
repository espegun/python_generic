import time

countdown = 5
while countdown > 0:
    countdown = countdown-1
    time.sleep(1)
    print(f"Sleep for {countdown} more seconds {countdown * '.'}", end="\r")

# Note that \r means print from the start of the line, i.e. oldest dots don't get erase even if countdown decreases

print("\nThat was fun.")
