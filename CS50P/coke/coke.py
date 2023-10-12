s = 50
k = 0
while k < s:
    ans = s - k
    print(f"Amount Due: {ans}")
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        k += coin
print(f"Change Owed: {k - s}")
