def theirPi(iters):
    ''' Calculate an approximation of PI using the Leibniz
    approximation with iters number of iterations '''
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1  # alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = theirPi(10000)
print(pi_approx)

def myPi():
    x = 1.0
    y = 3.0
    pi = 1.0
    for i in range(3, 10000, 4):
        pi = pi - (1/float(i)) + (1/(float(i+2)))
    return pi*4.0
    
print(myPi())
