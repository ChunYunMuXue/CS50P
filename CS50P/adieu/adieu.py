name = []
while True:
    try:
        s = str(input())
        if(s == ''):break
        name.append(s)
    except EOFError:
        break
print("Adieu, adieu, to ",end='')
c = 0
if(len(name) == 1):
    for si in name:
        print(si,end='')
else:
    for si in name:
        c += 1
        if(len(name) > 2 and c >= 2):print(",",end = '')
        if(c == len(name)):
            print(f" and {si}",end='')
        else:
            if(c > 1):
                print(f" {si}",end='')
            else:print(si,end='')