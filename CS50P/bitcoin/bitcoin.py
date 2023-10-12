import sys
import requests
if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit("Missing command-line argument")
try:
    s = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit("Command-line argument is not a number")
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
a = response.json()
rat = a["bpi"]["USD"]["rate"]
rat = rat.replace(',','')
print(f"${s * float(rat):,.4f}")