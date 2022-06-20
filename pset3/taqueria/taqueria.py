
menus = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0
while True:
    try:
        item = input("Item: ")
    except EOFError:
        print("")
        break
    item = item.strip().title()
    try:
        menus[item]
    except KeyError:
        pass
    else: # else block will run if try was successfull(without exeptions)
        cost = cost + menus[item]
        print(f"${cost:.2f}")


