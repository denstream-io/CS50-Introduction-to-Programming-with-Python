


greeting = input("Greeting: ")
greeting = greeting.strip()

if "Hello" in greeting:
    print("$0")
elif greeting[0] == "H":
    print("$20")
else:
    print("$100")