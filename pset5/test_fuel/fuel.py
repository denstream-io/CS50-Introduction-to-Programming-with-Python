
def main():
    while True:
        fraction = input("Fraction: ")
        (x, y, z) = fraction.partition("/")
        if not x.isdigit() or not z.isdigit():
            continue
        x = int(x)
        z = int(z)
        if z < x:
            continue
        else:
            percentage = convert(f"{x}/{z}")
            print(f"{gauge(percentage)}")
        break


def convert(fraction):
    (x, z) = fraction.split("/")
    if not x.isdigit() or not z.isdigit():
        raise ValueError
    x = int(x)
    z = int(z)
    if z == 0:
        raise ZeroDivisionError
    return (x/z) * 100
    
def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage:.0f}%"



if __name__ == "__main__":
    main()