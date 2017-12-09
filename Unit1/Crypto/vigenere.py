"""Vigenere module"""

from helpers import alphabet_position, rotate_character, validate
def encrypt(msg, key):
    """encrypt message with key"""
    key_pos_list = []
    new_msg = ""
    num = 0
    for char in key:
        key_pos_list.append(alphabet_position(char))
    for char in msg:
        new_msg += rotate_character(char, (key_pos_list[num%len(key_pos_list)]))
        if char.isalpha():
            num += 1
    return new_msg

def main():
    """Vigenere main encapsulation"""
    from sys import argv
    message = input("Type a message: \n")
    prompt = "Encryption key:\n"
    crypt_key = validate(prompt, *argv)
    print(encrypt(message, crypt_key))


if __name__ == "__main__":
    main()
