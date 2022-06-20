
HOUR = 60

def main():
    time = input("What time is it? ")
    time = convert(time)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / HOUR
    return hours + minutes


if __name__ == "__main__":
    main()