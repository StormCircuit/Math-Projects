import argparse








	#once we finish getting our polynomial, calculate its derivative and store it.
	#this is only needed for newtons method
def makeDx():
	#list x is passed in when we calculate it the first time
	global x
	global dx						#decrement degree
	dx = x[:]						#copy list
	i=0
	for i in x:
		dx[i] = x[i]*i				#multiply by its index (also our degree of X)
	del dx[0]
	return						#We do not return anything because we are manipulating the global variable.







#our two functions to calculate for any given x, we call x: j instead.
def dF(j):
	global dx
	return sum((a*j**i for i,a in enumerate(dx)))




def F(j):				
	global x
	return sum((a*j**i for i,a in enumerate(x)))







#for newtons method

#NOTES:
#WE NEED TO DEFINE A Df FOR OUR GIVEN f(x), this MUST BE DYNAMIC!

def newtonsMethod(x0,maxIt):

	#Get temp Xn.
	xn = x0

	for n in range(0, maxIt):
		fxn = F(xn)
		if fxn == 0:
			return xn, n, True	 #fxn is our root, n is steps taken, True indicates a solution was found.	   
		
		#else get f(x) prime for current Xn
		Dfxn = dF(xn)
		xn = xn - fxn/Dfxn

	#at this point we have exhausted all iterations.
	return xn, n, False








#m = a - f(a)*(b - a)/(f(b) - f(a))

def secantMethod(a,b,N):
	a = a
	b = b
	for n in range(1,N+1):

		#our calculatronadoodle where we get our current guess
		m = a - F(a)*(b - a)/(F(b) - F(a))

		#torture the computer a little less and store F(m) as variable fm1
		fm = F(m)

		#root check
		if fm == 0:
			return m, n, True

		#check do our checks to push m to a or b respectively.
		elif F(a)*fm < 0:
			a = a
			b = m
		elif F(b)*fm < 0:
			a = m
			b = b
	return m, n, False










#bsection method begins here. This works, more or less.
def bisectionMethod(a,b,maxIt):
	c = (a+b)/2.0

	i = 0

	for i in range(maxIt):
		c = (a+b)/2
		
		#zero check, if we hit the root exactly
		if F(c) == 0:
			return c, i, True 
		#now we do the proper algorithmic bit. If the signs are different (it is negative)
		#otherwise they are the same.
		if (F(c)*F(a) < 0):
			b = c
		else:
			a = c
	#if loop ends, return last c as root and i as iteration number. False means it did NOT suceed.
	return c, i, False













#global list for function
global x
global dx
x = []
dx = []

parser = argparse.ArgumentParser()

mode = parser.add_mutually_exclusive_group()
mode.add_argument("-newt", help="sets up for newton's method, mutually exclusive from -sec", action="store_true")
mode.add_argument("-sec", help="sets up for secant method, mutually exclusive from -newt", action="store_true")
parser.add_argument("-maxIt", type=int, help="max iterations.", default=10000)
parser.add_argument("initP", type=float, help="Initial point 1")
parser.add_argument("initP2", type=float, help="Initial point 2, if using newtons, it can be any number")
parser.add_argument("polyFileName", type=str, help="File name of polynomial")

args = parser.parse_args()

with open(args.polyFileName, 'r') as file:
	data = file.read().replace('\n', ' ')																	#modifes in global scope
	x = list(map(int, data.split()))
   #at this point x should be a 'list' (array)

del x[0] 	#gets rid of the user given degree, we're gonna use the index as our degree
x = x[::-1]		#reverse our array so this way index corresponds to degree. Where index 0 is now our coefficient



if args.newt:
	makeDx()
	print("running newtons")
	print(args.initP)
	print(args.maxIt)
	root, iterations, outcome = newtonsMethod(args.initP, args.maxIt)

elif args.sec:
	print("running secant")
	print(args.initP)
	print(args.initP2)
	print(args.maxIt)
	root, iterations, outcome = secantMethod(args.initP, args.initP2, args.maxIt)

else:
	print("running bisection")
	print(args.initP)
	print(args.initP2)
	print(args.maxIt)
	root, iterations, outcome = bisectionMethod(args.initP, args.initP2, args.maxIt)


fileT1 = args.polyFileName.split('.')
fileName = fileT1[0] + ".sol"
openFile = open(fileName , "w")
openFile.write('{0} {1} {2}'.format(root, iterations, outcome))