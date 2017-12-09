#You have a thermostat that allows you to set the room to any
#temperature between 40 and 89 degrees.

#The thermostat can be adjusted by turning a circular dial. If you turn the
#dial all the way to the left, you will set the temperature to 40 degrees.
#If you turn to the right by one click, you will get 41 degrees.
#As you continue to turn to the right, the temperature goes up,
#and the temperature gets closer and closer to 89 degrees.
#But as soon as you complete one full rotation (50 clicks), the temperature
#cycles back around to 40 and starts over.

#Write a program that calculates the temperature based on
#how much the dial has been turned.
#You should prompt the user for a number of clicks-to-the-right
#(from the starting point of 40 degrees).
#Then you should print the current temperature.

clicks_str = input("By how many clicks has the dial been turned?")
#0->40 24->64 74->64 49->89 51->41 -1->89
clicks = int(clicks_str)
if clicks > 50:
    clicks = clicks % 50
elif clicks < 0:
    clicks = clicks + 50
clicks = 40 + clicks

print("The temperature is ", clicks)
#equation is y = x + 40
# TODO calculate the temperature, and report it back to the user
