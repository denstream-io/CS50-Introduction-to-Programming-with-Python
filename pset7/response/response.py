from validator_collection import validators, errors


try:
    validators.email(input("email: "))
    print("Valid", end="")
except Exception:
    print("Invalid", end="")