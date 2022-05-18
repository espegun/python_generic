import re

PATTERN = r"jalla: (\d+) .*? strengen: (\".*?\")"

# findall captures all the groups as tuples in a list
# It looks for any number of matches in a text
with open("text.txt", "r") as f:
    text = f.read()

a = re.findall(PATTERN, text)
print(type(a))
print(a)


# matchs captures the full expression as group(0) and all the captured groups
# It needs to match from the START of the text string
with open("text.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    b = re.match(PATTERN, line)
    if b:
        print(type(b))
        print(b.groups())
        print(f"match.group(0), i.e. the full expression: {b.group(0)}")
        print(f"match.group(1), i.e. captured group 1: {b.group(1)}")
        print(f"match.group(2), i.e. captured group 2: {b.group(2)}")

print("That was fun.")
