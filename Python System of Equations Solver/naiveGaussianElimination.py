




def naiveGaussianElimination(matrixCoeff, matrixSoln):
	#we pass in matrixCoeff as a 2D array.
	#Matrix Soln will be a 1D array.
	#Before this is called we have already split the matrix into a solution vector and a coefficient matrix.
	
	#n will be our row counter. We will go from n to width
	#i will be our height counter. For every digit of N we will perform a loop for 'height' many times.
	#we will use a variable 'factor' to temp store the result of our division.
	
	n=0
	for j in matrixCoeff:
		i=n+1 																#correctly sets us to the n x n coordinate in the 2d array. 
																				#We can do n+1 as we are only zeroing the entries underneath any given row/column in the upper triangular matrix
		for j in matrixCoeff[i]:
			factor = float(matrixCoeff[n][i] / matrixCoeff[n][n])					#find common factor, store as a floating point number to reduce error.
			matrixCoeff[n][i] = (matrixCoeff[n][n] * factor) - matrixCoeff[n][i]	#calculate new entry for n,i in the matrix (should be 0 after this)
																				#calculate solution vector seperately
			matrixSoln[i] = (matrixSoln[n] * factor) - matrixSoln[i]

			i+=1
			#end loop
		n+=1																	#increment n by 1 to move to the next column.
																				#repeat inner loop 'matrixCoeff[0]' times. This just means we do it for every index of the column of our 2D array.

																				#once we find Xn we will put it in a matrix that is as large as the number of variables in our matrix.
																				#reuse n as variable we are solving for, i as height however we want Xn to be the nth element so we need to sync the variables
	

	n = len(matrixCoeff) - 1														#-1 due to array size in case I forget. At this point they are 'normalized'

	solnVector[n] = (matrixSoln[n] / matrixCoeff[n][n]) 						#keep an eye here, I think matrixSoln[n] should be matrixSoln[i]. Maybe I have it backwards.
	
	z = 0
	n-=1																								#puts us up and to the left in the matrix of the last variable. We are traveling along the diagonal.
	for k in matrixCoeff:
		tempRowCount = n + 1
		for tempRowCount in matrixCoeff:
			sumOfVariables = sumOfVariables + matrixCoeff[tempRowCount][n]*solnVector[tempRowCount]
			#end loop. This should iterate for the subsituted varibles

		solnVector[n] = (matrixSoln[n] - sumOfVariables) / matrixCoeff[n][n]							#calculates our variable then places it in its respective place in solnVector.
		n-=1																							#IE: X0 is in solnVector[0] (we start at X0 not X1) to make the algorithim easier.
	
	return solnVector																					#return solnVector. This way we can pass our array and ORIGINAL matrix Solution 
																										#vector and get X0, X1, etc out.