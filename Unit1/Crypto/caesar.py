"""caesar shift module"""
from helpers import rotate_character, validate #, alphabet_position

def encrypt(text, rot):
    """shift string rot positions"""
    new_text = ""
    for char in text:
        new_text += rotate_character(char, rot)
    return new_text

def main():
    """encapsuate execution main"""
    from sys import argv
    message = input("Type a message:\n")
    prompt = "Rotate by:\n"
    shift = int(validate(prompt, *argv))
    print(encrypt(message, shift))


if __name__ == "__main__":
    main()




# def encrypt(message, shift):
#     """encrypt message with specified shift"""
#     encrypted_message = ""
#     alpha = string.ascii_letters

#     for char in message:
#         if char not in alpha:
#             encrypted_message += char
#         else:
#             if (shift+alpha.find(char)) > 52:
#                 encrypted_message += chr(ord(char)+shift-26)
#             else:
#                 encrypted_message += chr(ord(char)+shift)

#     return encrypted_message
