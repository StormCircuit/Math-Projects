import sys
import random
import time
start_time = time.time()
#start time is used for calculating the time needed to run the algorithim.
#use sys to get runtime arguments.











#helper function to get current x-xn as well as keep track as to not redo steps
#'accumulates' current total so we dont do the other (x-xn) steps all over.
def accumulator(i, var, x):  
    currAcc = 1;  
    for j in range(i):  
        currAcc = currAcc * (var - x[j]);  
    return currAcc;





# Function for applying Newton's  
# divided difference formula is also calculated in here
def interpolate(var, x, y):
	#print(y)

	n = len(x)

	#calculating divided difference table
	for i in range(1, n):
		for j in range(n - i):
			y[j][i] = ((y[j][i-1] - y[j+1][i-1]) / (x[j]-x[i+j]));
	sum = y[0][0];

	#calls accumulator!!
	#final calculation
	for i in range(1, n):
		sum = sum + (accumulator(i, var, x) * y[0][i]);
	return sum;
  


































































#REDO ARG PASSING FOR INTERPOLATION!!!
#arg[1] will either be a number (the amount of points to RNG)
#OR arg[1] will be the file name!!!


#gets our first argument into arg0. This will either be a number or the file name.


#FOR INTERPOLATION: do a check if arg[1] is a number (integer check?)
	#if true then set a flag that we can check later to execute the RNG instead of file loading
	#if it is not an integer
try:
	arg0 = sys.argv[1]
	inputfile = arg0
	fileInputFlag = 1
except:
	fileInputFlag = 0

if fileInputFlag == 1:
	with open(inputfile, 'r') as inputfile:
		listOfPoints = [line.strip().split() for line in inputfile]


	listOfXPoints = listOfPoints[0]
	for i in range(len(listOfXPoints)):
		listOfXPoints[i] = float(listOfXPoints[i])





	#make into 2d matrix with first column being all the y values for div dif
	#eg [1][0] = F(x0), [2][0] = F(x1) so on
	listOfYPoints = listOfPoints[1]

	#initialize final matrix
	finalYMatrix = [[0 for i in range(len(listOfYPoints))] for j in range(len(listOfYPoints))]



	#convert our 1d array into a matrix for div differences
	for i in range(len(listOfYPoints)):
		finalYMatrix[i][0] = float(listOfYPoints[i])










	#RUNTIME LOOP FOR FILE MODE
	while True:

		varT = input("Please enter x to evaulate at: ")
		if str(varT) == "q":
			sys.exit()
		var = float(varT)


		answer = interpolate(var, listOfXPoints, finalYMatrix)
		print("Answer is: " + str(answer))













elif fileInputFlag == 0:
	generateThisManyPoints = input("Please enter number of points to generate: ")

	listOfXPoints = random.sample(range(1000000), generateThisManyPoints)

	listOfYPoints = random.sample(range(1000000), generateThisManyPoints)

	#initialize final matrix
	finalYMatrix = [[0 for i in range(len(listOfYPoints))] for j in range(len(listOfYPoints))]




	for i in range(len(listOfYPoints)):
		finalYMatrix[i][0] = float(listOfYPoints[i])





	listOfXEvaluate = random.sample(range(1000000), generateThisManyPoints)

	answer = []
	for i in range(generateThisManyPoints):
		answer.append(interpolate(listOfXEvaluate[i], listOfXPoints, finalYMatrix))

	print("Finished in %s seconds." % (time.time() - start_time))

	with open("solutionSet", 'w') as f:
		for i in range(generateThisManyPoints):
			f.write("(" + str(listOfXEvaluate[i]) + " , " + str(answer[i]) + ") " )
	print("Successfully wrote solution set to solutionSet file. Please make sure to move it before re-running!")