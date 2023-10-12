def main():
    print("Output: ", shorten(input("Input: ")))

def shorten(word):
    a = ""
    for i in word:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
            a = a + i
    return a

if __name__ == "__main__":
    main()