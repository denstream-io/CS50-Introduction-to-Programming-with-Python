import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    r_f = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

reader = csv.reader(r_f, delimiter=',')
next(reader, None) # skiping field name of original file
fieldnames = ["first", "last", "house"]


with open(sys.argv[2], "w") as w_f:
    writer = csv.DictWriter(w_f, fieldnames=fieldnames)
    writer.writeheader() # writing field names to new file

    for row in reader:
        name, house = row
        last, first = name.strip("\"\"").strip(" ").split(",")
        writer.writerow({'first': first.strip(" "), 'last': last, 'house': house})
r_f.close()
