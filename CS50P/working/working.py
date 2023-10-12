import re
import sys


def main():
    print(convert(input("Hours: ")))


def change(s):
    if(s.find(" ") == -1):
        raise  ValueError
        return None
    s1,s2 = s.split(" ")
    # print(s1)
    # print(s2)
    if(s1.find(':') != -1):
        ss1,ss2 = s1.split(":")
        ss1 = int(ss1)
        if(s2 == 'PM'):ss1 += 12
        if(ss1 == 12 and s2 == 'AM'):ss1 = 0
        if(ss1 == 24 and s2 == 'PM'):ss1 = 12
        if(ss1 <= 9):ss1 = str(f"0{ss1}")
        else: ss1 = str(ss1)
        if(int(ss2) >= 60):
            raise  ValueError
            return None
        if(int(ss1) > 24):
            raise  ValueError
            return None
        s = ss1 + ':' + ss2
    else:
        ss1 = int(s1)
        if(s2 == 'PM'):ss1 += 12
        if(ss1 == 12 and s2 == 'AM'):ss1 = 0
        if(ss1 == 24 and s2 == 'PM'):ss1 = 12
        if(ss1 <= 9):ss1 = str(f"0{ss1}")
        else: ss1 = str(ss1)
        if(int(ss1) > 24):
            raise  ValueError
            return None
        s = ss1 + ':00'
    return s

def convert(s):
    if(s.find("to") == -1):
        raise  ValueError
        return None
    a = re.search(r"^(.*:?.+\ (?:AM|PM))\ to",s)
    b = re.search(r"to\ (.*:?.+\ (?:AM|PM))$",s)
    if(not a or not b):
        raise  ValueError
        return None
    a = a.group(1)
    b = b.group(1)
    # print(a)
    # print(b)
    if(change(a) == None or change(b) == None):
        return None
    s = re.sub(a,change(a), s)
    s = re.sub(b,change(b), s)
    return s

if __name__ == "__main__":
    main()
