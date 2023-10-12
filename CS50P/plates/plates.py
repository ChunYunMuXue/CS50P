def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if(s[0].isalpha() and s[1].isalpha()):
            k = 0
            for a in s:
                if(not a.isalpha() and not a.isdigit()):return False
                if(a == '0' and k == 0):return False
                if(a.isdigit()):k = 1
                if(a.isalpha() and k):return False
            return True
    return False


if __name__ == "__main__":
    main()