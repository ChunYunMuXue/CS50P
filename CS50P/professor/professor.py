import random

def main():
    cnt = int(0)
    L = get_level()
    for i in range(10):
        t = 1
        x = generate_integer(L)
        y = generate_integer(L)
        for k in range(3):
            # print(f"TEST {k}")
            print(f"{x} + {y} = ",end = '')
            try:
                s = int(input())
            except ValueError:
                s = -1
            if(s != x + y):
                print("EEE")
            else:
                t = 0
                cnt = cnt + 1
                break
        if t:
            print(f"{x} + {y} = {x + y}")
    print("Score ",cnt)




def get_level():
    level = int(0)
    while True:
        try:
            level = int(input())
            if(level == 1 or level == 2 or level == 3):break
        except ValueError:
            continue
    return level


def generate_integer(level):
    if(level == 1):
        return random.randint(0,9)
    if(level == 2):
        return random.randint(10,99)
    if(level == 3):
        return random.randint(100,999)



if __name__ == "__main__":
    main()
