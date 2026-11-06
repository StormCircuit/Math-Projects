
def bisectionMethod(a, b, maxIt):
    i = 0
    while i <= maxIt:


    	#calculadoodle our new c.
        c = (a + b)/2.0


        if (F(a) * F(c)) < 0: 	#sign checking
            b = c
            
        else: 					#(func(b) * func(c)) > 0
            a = c
        i = i + 1

	#we now get out of loop and print the value of final c
	#i is the iteration number
	#c is current 'approx.'
    if abs((a-b)/2.0) == 0:
        return c, i, True 
    else:
    	return c, i, False 
