# Converts camelCase naming to snake_case

name = input("camelCase: ")
for i in name:
    if i.isupper():
        name = name.replace(i, "_" + i.lower())
print(f"snake_case: {name}")
