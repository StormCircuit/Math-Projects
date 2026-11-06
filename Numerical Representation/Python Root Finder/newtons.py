

#for newtons method

#NOTES:
#WE NEED TO DEFINE A Df FOR OUR GIVEN f(x), this MUST BE DYNAMIC!

def newtonsMethod(x0,maxIt):

    #Get temp Xn.
    xn = x0

    for n in range(0, maxIt):
        fxn = F(xn)
        if fxn == 0:
            return xn, n, True     #fxn is our root, n is steps taken, True indicates a solution was found.       
        
        #else get f(x) prime for current Xn
        Dfxn = dF(xn)
        xn = xn - fxn/Dfxn

    #at this point we have exhausted all iterations.
    return fxn, n, False