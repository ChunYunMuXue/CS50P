import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$",ip)
    if(not matches):
        return "False"
    try:
        for i in range(4):
            a = int(matches.group(i + 1))
            # print(a)
            if(a > 255 or a < 0):
                return "False"
        return "True"
    except ValueError:
        return "False"

if __name__ == "__main__":
    main()
