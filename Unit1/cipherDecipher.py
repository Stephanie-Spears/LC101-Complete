import string

def encrypt(message, shift):
    #alpha=string.ascii_lowercase
    encrypted_message=""

    for char in message:
        if char in string.punctuation or char in string.whitespace:
            encrypted_message += char
        else:
            encrypted_message += chr(ord(char)+shift)
    return encrypted_message

def decrypt(encrypted_message, shift):
    #alpha=string.ascii_lowercase
    decrypted_message=""

    for char in encrypted_message:
        if char in string.punctuation or char in string.whitespace:
            decrypted_message += char
        else:
            decrypted_message += chr(ord(char)-shift)
    return decrypted_message


message="Hello, World!"
shift = 1

print("Original: ", message)
encrypted_message = encrypt(message, shift)
print("Encrypted: ", encrypted_message)
decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted: ", decrypted_message)
