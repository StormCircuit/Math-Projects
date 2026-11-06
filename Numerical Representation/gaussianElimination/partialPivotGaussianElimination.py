def partialPivotGaussianElimination(unsolvedMatrix):       
                                                                            #this is our code to choose the pivot 
                                                                            #all we need to do is include it before we start eliminating
                                                                            #elements of a row in our naive code.
  uM = unsolvedMatrix                                                       #ease of access
  (height, width) = (len(uM), len(uM[0]))
  for y in range(0,height):
    maxrow = y
    for y2 in range(y+1, height):                            #Find max pivot
      if abs(uM[y2][y]) > abs(uM[maxrow][y]):                #if we find a row in our range (AKA our current column)
        maxrow = y2                                          

                                                             #the bit where we actually pivot, some dirty row swapping.
        (uM[y], uM[maxrow]) = (uM[maxrow], uM[y])            #swap the actual rows.
    for y2 in range(y+1, height):                            #eliminate current column, go down current column in th
      factor = uM[y2][y] / uM[y][y]
      for x in range(y, width):
        #print("\n")
        #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in uM]))  #debug statements, prints matrix
        uM[y2][x] -= uM[y][x] * factor                                                     #multiply by factor then subtract. Here we actually do the algebra.
        #print("Factor:" + str(factor))
  









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