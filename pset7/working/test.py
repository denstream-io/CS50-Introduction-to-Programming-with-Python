
def main():
    print(to_24(input("Date: ")))

def to_24(s):
    if s[-2: ] == "AM":
        if s[ :2] == "12":
            return str('00' + s[2:-2])
        else:
            return s[:-2]
    elif s[-2:] == "PM":
        if s[:2] == "12":
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:8]

if __name__ == "__main__":
    main()
#12:00 AM to 12:00 PM
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9 AM to 5 PM
# 9:00 AM to 5:00 PM
# 10 PM to 8 AM
# 10:30 PM to 8:50 AM

def seperate(time):
    if ":" in matches.group(1):
        hour, am_pm = time.split(" ")
        hour, minutes = hour.split(":")
        print(hour, minutes)
    else:
        hour, am_pm = time.split(":")
        print(hour, am_pm)
