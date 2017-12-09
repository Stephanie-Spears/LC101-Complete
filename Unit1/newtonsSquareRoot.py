def mySqrt(n):
    root = n/2
    #returns the right answer for 3 after five iterations, and for 10 it takes 7 iterations
    for i in range(7):
        newroot = .5 * (root + (n/root))
        root = newroot
    return newroot
        
    

print(mySqrt(100))
print(mySqrt(9))


