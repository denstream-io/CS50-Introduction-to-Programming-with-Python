from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len([ch for ch in s if ch.isdigit()])
    if s[0:2].isalpha() and len(s[0:2]) == 2 and len(s) <= 6 and str(s[n:][0]) != "0"\
    and (s[-n:].isdigit() or s[-n:].isalpha()) and not any(ch in punctuation for ch in s):
        return True

if __name__ == "__main__":
    main()