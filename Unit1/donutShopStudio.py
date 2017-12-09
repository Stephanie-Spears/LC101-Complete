print("Welcome to the Loop Hole!\nToday's Manager's Special is:\nCrunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Berries Oops All Berries")
      
userDonuts = float(input("How many would you like?"))
userPrice = float(input("How much would you like to pay per donut (suggested price is $4.35 each)?"))
tax = .05
userTotal = (userDonuts*userPrice) + (userDonuts*userPrice)*tax
#userTotal = str(round(((userTotal*tax)+userTotal),2))
print("Ok, let me prepare that for you...\nAfter tax, your total is: ${:.2f}, including your tax of:${:.2f}".format(userTotal, (userDonuts*userPrice*tax)))
