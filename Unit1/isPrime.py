##Write a function, is_prime, that takes a single integer
##argument and returns True when the argument is a prime
##number and False otherwise.
##
##As a refresher, a number is prime if it is not divisible by any
##other number (other than itself and 1). For example:
##2 is prime
##3 is prime
##4 is not prime because is is divisible by 2 
##5 is prime
##6 is not prime because it is divisible by 2 and 3
##7 is prime
##8 is not prime because it is divisible by 2 and 4
##9 is not prime because it is divisible by 3
##
##Also remember that you can use the modulo operator (%)
##to check whether one number is divisible by another.
##For example, here are a bunch of modulo operations on 12: 
##12 % 2 is 0
##12 % 3 is 0
##12 % 4 is 0
##12 % 5 is 2
##12 % 6 is 0 
##12 % 7 is 5
##12 % 8 is 4
##12 % 9 is 3
##
##Notice that 2, 3, 4, and 6, all the factors of 12, yield 0.
##This makes sense because modulo returns the remainder after division,
##and these numbers divide 12 perfectly, so there is no remainder left over. 
##
##Anyway, 12 is definitely not prime since it is divisible by a
##bunch of numbers: 2, 3, 4, and 6.
import math
def is_prime(n):
    if n <= 1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or n%(i+2)==0:
            return False
        i += 6
    return True

print("IS", is_prime(2))
print("IS", is_prime(3))
print("IS NOT", is_prime(4))
print("IS", is_prime(5))
print("IS NOT", is_prime(6))
print("IS", is_prime(7))
print("IS NOT", is_prime(8))
print("IS NOT", is_prime(9))
print("IS NOT", is_prime(12))
