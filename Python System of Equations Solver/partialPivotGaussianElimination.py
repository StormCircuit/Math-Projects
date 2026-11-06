def partialPivotGaussianElimination(matrixCoeff, matrixSoln):
  


  n = len(matrixCoeff)                                                      #use n again for the sake of consistency
  tempMatrix = matrixCoeff

  i = 0                                                                     #I forgot to comment why I did this, I changed b to matrixSoln to make it clearer
  for x in tempMatrix:                                                      #evaluate if this is useful or not
   x.append(b[i])
   i += 1

  for k in range(n):                                                        #row interchange, using n as our limit to our counter.
   for i in range(k,n):                                                     #i and k are our temporary variables
     if abs(tempMatrix[i][k]) > abs(tempMatrix[k][k]):                      #loop through every entry in every column then swap any pivots that are greater.
        tempMatrix[k], tempMatrix[i] = tempMatrix[i], tempMatrix[k]         #this is to perform the proper 'partial pivoting'
                                                                            #everything from here forth is just normal forward elimination followed by back substitution.



  n = 0
  for n in matrixCoeff:
    i = n + 1                                                                
                                                                            
    for i in matrixCoeff[n]:
      factor = float(matrixCoeff[n][i] / matrixCoeff[n][n])                 
      matrixCoeff[n][i] = (matrixCoeff[n][n] * factor) - matrixCoeff[n][i]  
                                                                            
      matrixSoln[i] = (matrixSoln[n] * factor) - matrixSoln[i]

      i+=1
      #end loop
    n+=1                                                                    #increment n by 1 to move to the next column.
                                                                            #repeat inner loop 'matrixCoeff[0]' times. This just means we do it for every index of the column of our 2D array.

                                                                            #once we find Xn we will put it in a matrix that is as large as the number of variables in our matrix.
                                                                            #reuse n as variable we are solving for, i as height however we want Xn to be the nth element so we need to sync the variables
  

  n = len(matrixCoeff) - 1                                                  #-1 due to array size in case I forget. At this point they are 'normalized'

  solnVector[n] = (matrixSoln[n] / matrixCoeff[n][n])                       #keep an eye here, I think matrixSoln[n] should be matrixSoln[i]. Maybe I have it backwards.
  
  z = 0
  n-=1                                                                      #puts us up and to the left in the matrix of the last variable. We are traveling along the diagonal.
  for z in matrixCoeff:
    tempRowCount = n + 1
    for tempRowCount in matrixCoeff:
      sumOfVariables = sumOfVariables + matrixCoeff[tempRowCount][n]*solnVector[tempRowCount]
                                                                                                #end loop. This should iterate for the subsituted varibles

    solnVector[n] = (matrixSoln[n] - sumOfVariables) / matrixCoeff[n][n]                        #calculates our variable then places it in its respective place in solnVector.
    n-=1                                                                                        #IE: X0 is in solnVector[0] (we start at X0 not X1) to make the algorithim easier.
  
  return solnVector 