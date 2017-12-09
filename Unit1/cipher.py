import string

def caesarShift(shh, encrypt):
    #adding the whitespace makes it so only the last whitespaces will be seen as punctuation...
    #so it just substitutes one whitespace for a different kind of whitespace. Sort of hard to see (ie: Run '\t' Rabbit)

    hush = ""
    mapLen = len(encrypt)
    for i in shh:
        index = encrypt.find(i)
        if index+2 > mapLen:
            index=-1
        hush += encrypt[index+1:index+2]

    print("original: ", shh)
    print("encrypted: ", hush)
    print("map of keys: ", encrypt)

shh = "Run Baby Rabbit!}~a s~a end"
encrypt=string.ascii_lowercase+string.ascii_uppercase+string.whitespace+string.punctuation

caesarShift(shh, encrypt)
