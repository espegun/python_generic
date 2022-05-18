import re
import json

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

### Make substitutiion string 
# \1 and \2 refers to capture groups
captured_info = []
for line in lines:
    if re.match(PATTERN, line):
        json_str = re.sub(PATTERN, r'{"jalla": \1, "strengen": \2}', line)  # JSON str, not dict
        captured_info.append(json.loads(json_str))  # Append, as a dict
print(captured_info)

print("That was fun.")
