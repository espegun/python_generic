import sys
import argparse


print("--- The simple approach with all positional arguments ---")
print(sys.argv)
print("")

print("--- Using the argsparser ---")

# https://docs.python.org/3/library/argparse.html (docs)
# https://docs.python.org/3/howto/argparse.html#id1 (tutorial)

parser = argparse.ArgumentParser()
# Required positional arguments
parser.add_argument("name", help="enter your name")
parser.add_argument("age", help="enter your age", type=int)
# Optional arguments (with full and short options)
parser.add_argument(
    "-v", "--verbose", help="add extra chit-chat", action="store_true"
)  # A flag: True if added, False if not
parser.add_argument(
    "-o", "--other_arg", help="also print this value"
)  # Saved as args.other_arg

args = parser.parse_args()
print(f"Hello, {args.name}, so you are {args.age} years old.")
if args.verbose:
    if args.age >= 40:
        print("Getting older, are we?")
    else:
        print("Still young and reasonable promissing!")
if args.other_arg:
    print(f"Here is another optional argument: {args.other_arg}")

print(
    "The argsparse module has far more depth than what is shown here, but this can get you far."
)

print("")
