

while True:
    (x, y, z) = input("Fraction: ").partition("/")

    try:
        x = int(x)
        z = int(z)
    except ValueError:
        continue

    try:
        percentage = (x/z) * 100
    except ZeroDivisionError:
        pass
    else:
        if percentage > 99 and percentage <= 100:
            print("F")
        elif percentage < 1:
            print("E")
        elif percentage > 100:
            continue
        else:
            print(f"{percentage:.0f}%")
        break
