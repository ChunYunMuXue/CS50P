import random
while True:
    try:
        n = int(input("Level: "))
        if(n > 0):break
    except ValueError:
        continue
goal = random.randint(1,n)
print(goal)
x = int(0)
while x != goal:
    try:
        x = int(input("Guess: "))
    except ValueError:
        continue
    if x < 1 : continue
    if x > goal : print("Too large!")
    if x < goal : print("Too small!")
    if x == goal :
        print("Just right!")
        exit()
