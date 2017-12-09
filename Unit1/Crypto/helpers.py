"""helper functions for crypto program"""
import string

def alphabet_position(letter):
    """find position of letter with 0-25 index"""
    return string.ascii_lowercase.find(letter.lower())

def rotate_character(char, rot):
    """return position of character rotated rot positions"""
    if char not in string.ascii_letters:
        return char
    else:
        new_char = string.ascii_lowercase[(alphabet_position(char)+rot)%26]
        if char.isupper():
            return new_char.upper()
    return new_char


def validate(prompt, *argv):
    """validate string input, given prompt"""
        # arg_str = ",".join(str(x) for x in argv)
        # print("string of args", arg_str)
    arglist = [x for x in argv] #convert argv from tuple to mutable list of strings, easier handling

    while True:
        try:
            astring = arglist[1]
        except IndexError:
            astring = input(prompt)

        if arglist[0] == "vigenere.py":
            valid_test = astring.isalpha()
            error_message = "Use only alphabetic characters for keyword."
        if arglist[0] == "caesar.py":
            valid_test = astring.isdigit()
            error_message = "Use only numeric values for rotation."

        if not valid_test:
            print(error_message, "Try again.")
            try:
                del arglist[1] #if there's an argv[2...], might cause bug. argv[2]--> becomes argv[1]. might be better to reassign and check for case
            except IndexError:
                continue
        else:
            return astring
