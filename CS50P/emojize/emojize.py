import emoji
name = input("Input: ")
pre = str()
las = str()
a = bool(0)
for s in name:
    if s == ':' : a = 1;
    if a :las += s
    else: pre.append(s)
print("Output: " + pre,end = '')
print(emoji.emojize(las))
