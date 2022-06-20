coke = 50
while True:
    amount = int(input("Insert Coin: "))
    if amount == 30:
        print(f"Amount Due: {coke}")
        continue
    coke = coke - amount
    if coke > 0:
        print(f"Amount Due: {coke}")
    else:
        print(f"Change Owed: {-1*coke}")
        break