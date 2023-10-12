def convert(time):
    a,b = time.split(":")
    time = float(a) + (float(b) / 60)
    return time

def main():
    time = input("What time is it?")
    time = convert(time)
    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")
if __name__ == "__main__":
    main()


