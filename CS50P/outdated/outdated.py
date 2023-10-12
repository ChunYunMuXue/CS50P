d = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
y = str()
r = str()
m = str()
now = str()
while True:
    name = input("Date: ")
    # print(name)
    if(name.find('/') != -1):
        m,r,y = name.split('/')
    else:
        if(name.find(',') != -1):
            now,y = name.split(',')
            m,r = now.split(' ')
            y.strip(' ')
            if m in d:
                m = int(d[m])
            else:
                continue
        else:
            continue
    try:
        r = int(r)
        y = int(y)
        m = int(m)
        if(m <= 12 and r <= 31):
            break
    except ValueError:
        continue
if(r < 10):
    r = str('0' + str(r));
if(m < 10):
    m = str('0' + str(m));
print(f"{y}-{m}-{r}")

