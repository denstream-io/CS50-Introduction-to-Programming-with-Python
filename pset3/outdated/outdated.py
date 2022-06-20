
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:

    format = input("Date: ")
    if "/" in format:
        format = format.split("/")
        try:
            day = int(format[1])
            month = int(format[0])
        except ValueError: # When string letters are converted to numbers
            pass
        else:
            day = int(format[1])
            year = format[2]
            if day > 31:
                continue
            elif month > 12:
                continue
            year = format[2]
            month = format[0]
            day = format[1]
            print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
            break
    elif " " in format:
        format = format.split(",")
        year = format[1]
        (month, day) = format[0].split(" ")
        try:
            month = months.index(month) + 1
            day = int(day)
        except IndexError:
            pass
        except ValueError:
            pass
        else:
            if day > 31:
                continue
            print(f"{year}-{month:02}-{day:02}")
            break