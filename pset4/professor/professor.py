# This program is unique
import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        number1 = generate_integer(level)
        number2 = generate_integer(level)
        try:
            solution = int(input(f"{number1} + {number2} = "))
        except ValueError:
            continue
        else:
            if number1 + number2 == solution:
                score += 1
                continue
            else:
                print("EEE")
                trials = 0
                for _ in range(2):
                    try:
                        solution = int(input(f"{number1} + {number2} = "))
                    except ValueError:
                        pass
                    if number1 + number2 == solution:
                        score += 1
                        break
                    else:
                        print("EEE")
                    trials += 1
                if trials == 2:
                    solution = number1 + number2
                    print(f"{number1} + {number2} = {solution}")
    print(f"Score: {score}")




def get_level():

    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n > 0 and n <= 3:
            return n


def generate_integer(level):
    levels = {
        1: (0, 9),
        2: (10, 99),
        3: (100, 999)
    }
    if level < 0 or level > 3:
        raise ValueError
    return random.randint(*levels[level]) # Intresting idea of unpacking


if __name__ == "__main__":
    main()



