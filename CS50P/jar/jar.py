import sys

class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self.c = capacity
        else:
            raise ValueError
        self.s = 0

    def __str__(self):
        s = ''
        for i in range(self.s):
            s += '🍪'
        return s
    def deposit(self, n):
        if(n + self.s > self.c):
            raise ValueError
        else:
            self.s += n
    def withdraw(self, n):
        if(self.s - n < 0):
            raise ValueError
        else:
            self.s -= n

    @property
    def capacity(self):
        return self.c

    @property
    def size(self):
        return self.s

def main():
    a = Jar()

if __name__=='__main__':
    main()
