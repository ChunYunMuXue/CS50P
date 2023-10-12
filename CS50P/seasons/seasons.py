from datetime import date
import re
import inflect
import sys

def main():
    print(did(input("Date of Birth: ")))


def did(s):
    si = si = re.search(r"^\d{4}\-\d{2}\-\d{2}$",s)
    if(not si):sys.exit('Invalid date')
    y,m,d = s.split('-')
    y = int(y)
    m = int(m)
    d = int(d)
    if(y < 0 or not (m <= 12 and m >= 1) or not(d <= 31 and d >= 1)):sys.exit('Invalid date')
    td = date.today()
    bd = date(y,m,d)
    rest = -(bd - td).days * 24 * 60
    inf = inflect.engine()
    w = inf.number_to_words(rest)
    w = w.replace(' and','').capitalize()
    w = w + ' minutes '
    return w

if __name__ == "__main__":
    main()
