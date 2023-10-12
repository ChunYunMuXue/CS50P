from pyfiglet import Figlet
import sys
from random import choice
figlet = Figlet()
L = figlet.getFonts()
if(len(sys.argv) == 3):
    if(sys.argv[1] != '-f' and sys.argv[1] != '--font'):
        print("Invalid usage")
        sys.exit("Invalid usage")
    else:
        s = sys.argv[2]
        figlet.setFont(font = s)
else:
    if (len(sys.argv) == 1):
        s = str(choice(L))
        figlet.setFont(font = s)
    else:
        print("Invalid usage")
        sys.exit("Invalid usage")
name = input("Input: ")
print("Output: ")
print(figlet.renderText(name))
