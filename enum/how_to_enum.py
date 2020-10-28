from enum import Enum

"""
Set symbolic names bound to unique, constant values.
https://docs.python.org/3/library/enum.html
"""



# Define
class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Colors.RED.name)  # RED
print(Colors.RED.value)  # 1
try:
    print(Colors.YELLOW)
except AttributeError:
    print("Could not find Colors.YELLOW.")

# Iterate though
for col in Colors:
    print(col.name, col.value)

# Comparison (these are all True)
print(Colors.RED is Colors.RED)
print(Colors.RED is not Colors.GREEN)
print(Colors.RED == Colors.RED)
print(Colors.RED != Colors.GREEN)


print("That was fun.")

