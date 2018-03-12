def get_name():
    name = str(input("What's your name?    "))
    x = True
    while x:
        name_no_space = name.replace(" ", "")
        if name_no_space.isalpha():
            return name
            x = False
        else:
            name = str(input("You speak english? What's your name?    "))

def print_name():
    name=get_name()
    print("Hello ", name)

print_name()