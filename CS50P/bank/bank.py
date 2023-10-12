str = input("Greeting: ")
str = str.strip()
str = str.lower()
if str.startswith("hello"):
    print("$0")
elif str.startswith("h"):
    print("$20")
else:
    print("$100")