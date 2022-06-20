import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

table = []
if sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")

print(tabulate(table, headers="keys", tablefmt="grid"))


# https://pypi.org/project/tabulate/
