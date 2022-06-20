import re

def main():
    print(count(input("Text: ")))

def count(s):
    return len(re.findall(r"\b[uU]m", s))

if __name__=="__main__":
    main()