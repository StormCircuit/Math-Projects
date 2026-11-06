#looks for our next empty cell, empty cells = 0.
def emptySrch(tArr,promCel): 
	for row in range(9): 
		for col in range(9): 
			if(tArr[row][col]==0): 
				promCel[0]=row
				promCel[1]=col 
				return True
	return False
  

#given a number, check if that number is in the row already.
#returns False if it is not (so it's boolean)
def rwChk(tArr,row,x): 
	for i in range(9): 
		if(tArr[row][i]==x): 
			return True
	return False
  
#same as row check (looks for a passed value, if it is in the column then return False)
def colChk(tArr,col,x): 
	for i in range(9): 
		if(tArr[i][col]==x): 
			return True
	return False
  
#checks the 3x3 'quadrant' our current number lies in.
#returns boolean
def chkQuadr(tArr,row,col,x): 
	for i in range(3): 
		for j in range(3):
			if(tArr[i+row][j+col]==x):
				#if found;
				return True
	return False


