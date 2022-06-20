import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    f = choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        s = input("Input: ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(s))
    else:
         sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


