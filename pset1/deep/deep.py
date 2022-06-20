question = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
question = question.strip().lower()

if question in ["forty two", "forty-two", "42"]:
    print("Yes")
else:
    print("No")