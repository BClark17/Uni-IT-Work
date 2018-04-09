HEXADECIMAL_COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "Black": "#000000", "BLUEVIOLET": "#8a2be2",
                       "CORAL": "#ff7f50", "CYAN1": "#00ffff", "DARKGREEN": "#006400"}

while True:
    colour = input("Enter Colour Name: ")
    colour = colour.upper()
    counter = 0
    if colour in HEXADECIMAL_COLOURS:
        print(colour, 'is Hexadecimal code: ', HEXADECIMAL_COLOURS[colour])
        break
    else:
        print("Invalid Colour Name, please try again")
print("Program Terminated")
