d = {}
k = []
while True:
    try:
        name = input()
        if(name == ''):break
        if(name in d):
            d[name] = d[name] + 1
        else:
            d[name] = int(1)
            k.append(name)
    except EOFError:
        break
k.sort()
for name in k:
    now = name.upper()
    print(f"{d[name]} {now}")
