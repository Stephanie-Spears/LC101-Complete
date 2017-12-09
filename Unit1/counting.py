"""program to count occurance of each letter in a file"""


def count_char(text):
    """count char in text"""
    alpha_dict = {}
    for char in text:
        alpha_dict[char] = 0
    for char in text:
        if char in alpha_dict:
            alpha_dict[char] += 1
    return alpha_dict

def reverse_dict(a_dict):
    """reverse keys and values of dictionaries"""
    new_dict = {}
    for (key, val) in a_dict.items():
        new_dict[val] = key
    return new_dict

def factors_dict(num):
    """generate dictionary, keys=num, val=factors of num"""
    a_dict = {}
    while num > 0:
        a_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                a_list.append(i)
        a_dict[num] = a_list
        num -= 1
    return a_dict



def main():
    """main"""
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

    alpha_dictionary = count_char(text)
    for (key, val) in alpha_dictionary.items():
        print("Original", key + ": ", val)

    reverse_dictionary = reverse_dict(alpha_dictionary)
    for (key, val) in reverse_dictionary.items():
        print("Reversed", str(key) + ": ", val)

    print("Factors", factors_dict(15))

if __name__ == '__main__':
    main()
