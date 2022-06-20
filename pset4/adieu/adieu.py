import inflect # Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words
p = inflect.engine()

names = ()
while True:
    try:
        name = input("Name: ")
    except EOFError:
        adieu = p.join(names)
        print(f"Adieu, adieu, to {adieu}")
        break
    names = names + (name,)

