
groceries = {}

while True:
    try:
        grocery = input("")
    except EOFError: # When user input is empty
        for (key, value) in sorted(groceries.items()):
            print(value, key)
        break
    grocery = grocery.strip().upper()
    try:
        groceries[grocery]
    except KeyError:
        groceries[grocery] = 1
    else:
        groceries[grocery] += 1

