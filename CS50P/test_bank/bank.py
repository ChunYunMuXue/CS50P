def main():
    str = input("Greeting: ")
    print(value(str))

def value(str):
    str = str.strip()
    str = str.lower()
    if str.startswith("hello"):
        return 0
    elif str.startswith("h"):
        return 10
    else:
        return 100

if __name__ == "__main__":
    main()