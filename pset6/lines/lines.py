import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
lines = 0
if sys.argv[1].endswith(".py"):
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")

for line in f:
    if line.lstrip().startswith("#"): # checks for lines that starts with "#"
        pass
    elif line.isspace(): # checks for empty space
        pass
    else:
        lines += 1

print(lines)

f.close()

