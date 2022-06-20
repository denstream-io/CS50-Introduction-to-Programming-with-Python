


def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("H") and not greeting.startswith("Hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()