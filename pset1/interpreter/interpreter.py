


interpreter = input("Expression: ")
x, y, z = interpreter.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)