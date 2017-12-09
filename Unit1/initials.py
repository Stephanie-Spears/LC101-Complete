def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    for i in range(len(fullname)):
        index = fullname.find(" ")
        newName = fullname.capitalize()
        newName = fullname[index+1:].capitalize()
        #print(fullname)
        print(newName)
    
get_initials("Ozzie Smith")
get_initials("Bonnie blair")
get_initials("George G")
get_initials("Daniel Day Lewis")
get_initials("xaniel xay xewis")
    # TODO your code here

    
#Your function will receive one argument – fullname, a string representing someone’s name
# – and should return a string with that name’s capitalized initials.

#Here are some examples of what your function should return for various fullname arguments:

#fullname	return value
#Ozzie Smith	OS
#Bonnie blair	BB
#George	G
#Daniel Day Lewis	DDL

#Even if the name starts with a lowercase letter, you should always capitalize the initials.
#For example, notice how even if fullname == "Bonnie blair", you should still return "BB" rather than "Bb"
#If you were to invoke your function and print the result, it would look something like this:
#ozzie_inits = get_initials("Ozzie Smith")
#print("The initials of 'Ozzie Smith' are", ozzie_inits)
# => prints "The initials of 'Ozzie Smith' are OS"

#Hint
#You’ll need to collect the initials as you find them, and return them all together at the end.
#You may want to re-read about The Accumulator Pattern.


##Let’s now turn this into an interactive program that a user can run from the terminal. All you have to do is add an input statement to ask the user for his/her name, and then a print statement to report the results back to him/her. Your program should work like this:
##
##$ python initials.py
##What is your full name?
##Ozzie Smith
##OS
##Just to be clear about the example above:
##
##The user typed the first line, causing the program to run.
##Then, the program printed the second line asking for their name.
##Then the user typed the third line (“Ozzie Smith”).
##Finally, the program printed the initials (“OS”).
##Make it Importable
##Almost done! There is one more thing you must do before submitting. Presumably, your file now looks like this:
##
##def get_initials(fullname):
##    # some code here
##
### some more code here (input and print statements)
##As you know, the second block of code contains the lines that actually get executed when the user runs the script. The code inside the get_initials function, by contrast, only executes thanks to the fact that it gets invoked by one of the statements from that second block of code that sits all the way on the left, at the global level of scope.
##
##Generally speaking, however, it is actually bad practice to have “loose” statements floating around at that left-most, unindented scope of a script. There are two reasons why:
##
##Issue 1: Organization. As your script grows larger, it can become hard to keep track of all those loose statements, especially if you don’t keep them all together in one block. At that point, you will start to loose track of exactly what happens when the script is run.
##
##Issue 2: Importing. When some other file tries to import this file, all the loose statements will be executed, which is probably not what the other file wanted. For example, say you are writing another script, and you once again encounter the need to parse initials from people’s names. Instead of re-writing the get_initials function, this is a perfect chance to reuse the code you have already written by importing your initials.py file. Sounds great! But unfortunately, the moment you import the file, those input and print statements will blurt out and start talking to the user.
##
##The solution to Issue 1 is to move your input and print statements into a main function, like this:
##
##def get_initials(fullname):
##    # some code here
##
##def main():
##    # some more code here (input and print statements)
##
##main()
##In the new version, notice that we have placed the second block of code inside a function called main. This is the generally accepted pattern: Move all loose statements into a main function so that you have them together in one place. Finally, the only loose statement left is the invocation of main at the end.
##
##Issue 2 can be solved by adding one more line of code that places the main() invocation inside a (strange-looking) if statement:
##
##def get_initials(fullname):
##    # some code here
##
##def main():
##    # some more code here (input and print statements)
##
##if __name__ == '__main__':
##    main()
##In effect, that conditional says:
##
##“If this is actually the main program that is being run, then go ahead and execute the main function. Otherwise, if this file is being imported, or something else is going on, then stay quiet and do nothing.”
##Note
##If you are curious about the if __name__ == '__main__': conditional, you can check out this Stack Overflow post.
##Now we are good to go! The program works normally when run directly from the command-line, but if some other file imports it, the main function will not execute.
##
##Warning
##Before you submit your work, it is important that you transform your initials.py code to reflect the example above. The grading script is going to import your file, and if you have a loose input statement at the global scope level, that statement is going to execute and wait forever for input from a non-existent user, and you will find yourself waiting a very long time for your grade.
##How to Submit
##The submission process for this assignment is slightly different from that of your previous assignments. You will not be given a premade starter file into which you can paste your code. Instead, you must upload your own file into the workspace.
##
##Click the Upload button on the top-left of the Vocareum window, and select your initials.py file.
##Click Submit!
