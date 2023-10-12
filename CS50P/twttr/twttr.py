str = input("Input: ")
print("Output: ",end = '')
for a in str:
    if a.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(a,end = '')