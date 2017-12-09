def sumTo(n):
    mysum = 0
    while n != 0:
        mysum += n
        n = n-1
        sumTo(n)
    else:
        return mysum 
    # your code here
print(sumTo(10))
