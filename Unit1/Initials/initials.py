""" return initials of name:
get_init(string name):
    initialize newName based on string name parameter
    mod newName to contain only caps all first letters of names
    return string newName

main():
    user input/output
    astring = get_init(string name)
    alist.append(astring)
    return alist
"""

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    a_init = ""
    for char in fullname.title():
        if char.isupper():
            a_init += char
    return a_init


def main():
    """ Encapsulation of program in main() """
    name_string = input("What is your full name?")
    #a_list = []
    #for i, item in enumerate(name_list, 1):
    #for i in range(len(name_list)):
    a_string = get_initials(name_string)
    print(a_string)
    #print("The initials of '{:}' are".format(name_string), a_string)

    #return a_string
    #a_list.append(a_string)
    #print("The initials of '{:}' are".format(name_list), a_string)
    #return a_list

#ifndef
if __name__ == '__main__':
    main()

""" initials.py module docstring header:
Your function will receive one argument – fullname, a string representing someone’s name – and should return a string with that name’s capitalized initials.
Even if the name starts with a lowercase letter, you should always capitalize the initials. For example, notice how even if fullname == "Bonnie blair", you should still return "BB" rather than "Bb"
You may assume that the name will contain only letters (uppercase and/or lowercase) plus single spaces between words. This means you don’t have to worry about Conan O’Brien, T.S. Eliot, or Cee-Lo Green.
ozzie_inits = get_initials("Ozzie Smith")
print("The initials of 'Ozzie Smith' are", ozzie_inits)
# => prints "The initials of 'Ozzie Smith' are OS"

You’ll need to collect the initials as you find them, and return them all together at the end
You must run python from your lc101/initials directory for the import command to work.

Let’s now turn this into an interactive program that a user can run from the terminal. All you have to do is add an input statement to ask the user for his/her name, and then a print statement to report the results back to him/her. Your program should work like this:

$ python initials.py
What is your full name?
Ozzie Smith
OS
Just to be clear about the example above:

The user typed the first line, causing the program to run.
Then, the program printed the second line asking for their name.
Then the user typed the third line (“Ozzie Smith”).
Finally, the program printed the initials (“OS”).
"""
