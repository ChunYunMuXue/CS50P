while True:
    try:
        print("Fraction: ",end = "")
        name = str(input())
        x,y = name.split('/')
        x = int(x)
        y = int(y)
        # print(x,y)
        while x > y or y == 0:
            print("Fraction: ",end = "")
            name = str(input())
            x,y = name.split('/')
            x = int(x)
            y = int(y)
            # print(x,y)
            # print(now);
        now = x / y
        now = now * 100
        now = round(now)
        # print(now)
        now = format(now,".0f")
        now = int(now);
        # print(now != 0 and now != 100)
        if now > 1 and now < 99:
            print(f"{now}%")
        else:
            if(now <= 1):
                print("E")
            if(now >= 99):
                print("F")
    except ValueError:
        print("",end = "")
    except ZeroDivisionError:
        print("",end = "")
    else:
        break
