import sys
from tabulate import tabulate
if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit("Too many command-line arguments")
s = sys.argv[1]
table = []
if(s.find('.') == -1):
    print("Not a CSV file")
    sys.exit("Not a CSV file")
a,b = s.split('.')
if(b != 'csv'):
    print("Not a CSV file")
    sys.exit("Not a CSV file")
try:
    with open(s,'r') as file:
        for line in file:
            row = line.rstrip().split(",")
            table.append(row)
except FileNotFoundError:
    print("File does not exist")
    sys.exit("File does not exist")
print(tabulate(table, headers='firstrow', tablefmt='grid'))