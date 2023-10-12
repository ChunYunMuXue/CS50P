s = input("camelCase: ")
s = s.strip()
for a in s:
    if a.isupper():
        print('_',end='')
        print(a.lower(),end='')
    else:
        print(a.lower(),end='')
