

input_ = input()



def convert(input_):

    if ":)" or ":(" in input_:
      return  input_.replace(":)","🙂").replace(":(","🙁")


def main(input_):
    output = convert(input_)
    print(output)

main(input_)