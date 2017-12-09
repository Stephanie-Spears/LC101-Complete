#Write a function that receives a string argument, and returns a "mirrored" version of the string.

def mirrorInput(someString):
    newString = someString
    i = len(someString)
    while i > 0:
        newString += someString[i-1]
        i = i -1
        
    return newString

someString = input("input string: ")

print(mirrorInput(someString))
