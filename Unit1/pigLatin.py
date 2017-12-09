def piggieWord(text):
    pigLat = "ay"
    first_letter=text[0]
    first_letter = first_letter.lower()
    if first_letter in "aeiou":
        return text + "ay"
    else:
        return text[1:] + text[0] + pigLat

def piggieSentence(text):
    list_of_words = text.split(" ")
    new_sentence = ""
    for word in list_of_words:
        new_sentence = new_sentence + piggieWord(word)
        new_sentence = new_sentence + " "
    return new_sentence

print("SHOULD BE: 'ythonpay odecay insway'", piggieSentence("python code wins"))
print("SHOULD BE: 'allay openay androidsay'", piggieSentence("all open androids"))
