import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

