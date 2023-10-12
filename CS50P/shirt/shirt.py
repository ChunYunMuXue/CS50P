from PIL import Image,ImageOps
import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit("Too many command-line arguments")

IN = sys.argv[1]
OUT = sys.argv[2]

inp,ina = IN.split('.')
outp,outa = OUT.split('.')
if(not ina in ['jpg','png','jpeg']):
    print("Invaild input")
    sys.exit("Invaild input")
if(outa != ina):
    print("Input and output have different extensions")
    sys.exit("Input and output have different extensions")
shirt = Image.open("shirt.png")
try:
    with Image.open(IN) as file:
        file = ImageOps.fit(file,shirt.size)
        file.paste(shirt,shirt)
        file.save(OUT)
except FileNotFoundError:
    print("File does not exist")
    sys.exit("File does not exist")
