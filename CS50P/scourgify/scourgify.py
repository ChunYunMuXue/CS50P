import sys
import csv
from tabulate import tabulate
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit("Too many command-line arguments")
s1 = sys.argv[1]
s2 = sys.argv[2]

table = []
house = str()

x = s1
y = s2

try:
    with open(s1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            n1,n2 = row["name"].rstrip().split(", ")
            house = row["house"].strip('\n')
            table.append({"first":n2,"last":n1,"house":house})
except FileNotFoundError:
    print(f"Could not read {s1}")
    sys.exit(f"Could not read {s1}")
try:
    with open(s2,"w",newline='') as file:
        write = csv.DictWriter(file,fieldnames=["first","last","house"])
        write.writeheader()
        for line in table:
            write.writerow({"first":line["first"],"last":line["last"],"house":line["house"]})
except FileNotFoundError:
    print(f"Could not read {s2}")
    sys.exit(f"Could not read {s2}")