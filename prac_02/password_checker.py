"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """"Determine if the provided password is valid."""
    if 6 < len(password) < 2:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.isdigit():
            count_digit += 1
            print("digit", count_digit)
        elif char.islower():
            count_lower += 1
            print("lower ",count_lower)
        elif char.istitle():
            count_upper += 1
            print("upper ",count_upper)
        else:
            char_password = char
            for char in SPECIAL_CHARACTERS:
                if char == char_password:
                    count_special += 1
                    print("special ",count_special)
        pass

    # TODO: if any of the 'normal' counts are zero, return False
    if count_digit == 0:
        print("You password needs at least one digit.")
        return False
    elif count_lower == 0:
        print("You password needs at least one lowercase.")
        return False
    elif count_upper == 0:
        print("You password needs at least one uppercase.")
        return False
    elif count_special == 0:
        print("You password needs at least one special character.")
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()