def naiveGaussJordan(unsolvedMatrix):


#x and y are exactly what they sound like
#y2 is a temp variable to handle the column
#factor is also exactly what it sounds like, the number we're multipling by to reduce.
#also I got tired of writing 'unsolvedMatrix' so "uM" is our variable holding it.

  uM = unsolvedMatrix
  (height, width) = (len(uM), len(uM[0]))                    #DEDUCE with FACTS and LOGIC our height and width
  for y in range(0,height): 
    maxrow = y
    for y2 in range(y+1, height):                            #eliminate current column, go down current column
      factor = uM[y2][y] / uM[y][y]
      for x in range(y, width):
        #print("\n")
        #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in uM]))  #debug statements, prints matrix
        uM[y2][x] -= uM[y][x] * factor                      #multiply by factor then subtract. Here we actually do the algebra.
        #print("Factor:" + str(factor))
  
                                                            #we need to handle non-square matrices here.
  
  for y in range(height-1, 0-1, -1):
    factor = uM[y][y]
    for y2 in range(0,y):
      #here we start subbing for rows.
      for x in range(width-1, y-1, -1):
        uM[y2][x] -=  uM[y][x] * uM[y2][y] / factor
      #here we actually do the algebra to calculate our final Xn
    uM[y][y] /= factor
    for x in range(height, width):                        #Normalize row y
      uM[y][x] /= factor
  return uM                                               #return "uM" as our matrix. Thus we can call our function and have it equal to 'solvedMatrix' in our main routine.
                                             #return "uM" as our matrix. Thus we can call our function and have it equal to 'solvedMatrix' in our main routine.