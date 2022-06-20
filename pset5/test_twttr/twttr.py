

def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(i, "")
    return f'{word}'

if __name__ == "__main__":
    main()