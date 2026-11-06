import sys
from sudokuHelper import emptySrch, rwChk, colChk, chkQuadr
import time
start_time = time.time()

try:
	arg0=sys.argv[1]
except Exception:
	print("ERROR! No argument given! Please execute as 'python sudokuSolver.py yourFilenameHere' including file extensions")
	print("If your file name is mySoduku.txt you would use 'python sodokuSolver.py mySoduku.txt'")
	print("Exiting program...")
	sys.exit()												
#gets our first argument into arg0, throws an error if none passed.



#soduku solver. no checking if the given problem is invalid so don't try that
def solver(tArr):
	#initiates temp list for promising cell, keeps track of our location we are at.
	promCel=[0,0] 
	  
	#Checks if there is an empty location, if there is NOT an empty location
	#BREAK THE LOOP
	#else continue	 
	if(not emptySrch(tArr,promCel)): 
		return True
	  
	#assign temp values  
	row=promCel[0] 
	col=promCel[1]

	#kick off main checks
	for x in range(1,10):
		# if looks promising 
		if(not rwChk(tArr,row,x) and not colChk(tArr,col,x) and not chkQuadr(tArr,row - row%3,col - col%3,x)): 
			  
			#get temp assignment 
			tArr[row][col]=x 
  
			#success condition, recursively call our current tArrangement
			#it will work on that until it suceeds or fails. It returns false below
			#outside this loop which then brings us to tArr[row][col]=0
			if(solver(tArr)): 
				return True
  
			#if all else fails set to 0, then return false below 
			tArr[row][col] = 0
			  
	#goes back up the recursion stack if it fails and tries the next number		 
	return False 
  


with open(arg0, 'r') as inputfile:
	gridT = [line.strip().split() for line in inputfile]

grid = [[int(int(j)) for j in i] for i in gridT]


solver(grid)

#prints results
print("", end= ' ')
for i in range(9): 
	for j in range(9):
		if j in [3, 6]:
			print('|', end=' '),
		print(grid[i][j], end=' '),
	print('\n', end= ' ')
	if i in [2, 5]:
		print ('------+-------+------\n', end=' '),
print("Done in %s secs" % (time.time() - start_time))


#code to create a solution file,
#if you want to create a solution file just delete the three hyphons below this line
#AND
#at the bottom of this block of code

#three hyphons underneath this line
"""

with open(time.strftime("%Y-%m-%d-%H:%M")+"-SudokuSol.sol", 'w') as f:
	for i in range(9): 
		for j in range(9):
			if j in [3, 6]:
				f.write('| '),
			f.write(str(grid[i][j])+" "),
		f.write('\n')
		if i in [2, 5]:
			f.write('------+-------+------\n'),

	f.write("---------9x9 matrix representation---------\n")
	for i in range(9):
		for j in range(9):
			f.write(str(grid[i][j])+" "),
		f.write('\n')

#delete these three hyphons as well
"""