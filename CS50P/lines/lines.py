import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit("Too many command-line arguments")
s = sys.argv[1]
if(s.find('.') == -1):
    print("Not a Python file")
    sys.exit("Not a Python file")
a,b = s.split('.')
if(b != 'py'):
    print("Not a Python file")
    sys.exit("Not a Python file")
try:
    with open(s,'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File does not exist")
    sys.exit("File does not exist")
cnt = int(0)
for line in lines:
    k = int(0)
    for c in line:
        if(k == 0 and c == '#'):break
        if(c != ' ' and c != '\n'):
            # print(f"this is {c}")
            # print(c == ' ')
            k = 1
    cnt += k
    # print(line,cnt)
print(cnt)