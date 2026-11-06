import sys 																		#use sys to get runtime arguments.
import naiveGaussianElimination as nGE
import partialPivotGaussianElimination as pPGE 									#imports our gaussian elimination methods. May also need to import some sort of print file routine.

arg0 = sys.argv[1]																#gets our first argument into arg0. This will either be --spp (CASE SENSITIVE!) or the file name.



try:
    arg1 = sys.argv[2]																#do a check to see if we got  2 arguments passed. This is effectively checking to see if we got passed --spp at runtime
    spp = 1
except IndexError:	
	spp = 0
	pass

if spp == 1:																		
	inputfile = sys.argv[2]
	print("performing partial pivoting")
else:
	print("performing naive")
	inputfile = sys.argv[1]


with open(inputfile, 'r') as inputfile:
    loadedMatrix = [line.strip().split() for line in inputfile]

unsolvedCoeffMatrix = [[float(float(j)) for j in i] for i in loadedMatrix]	#finally we convert our vector and matrix to floats
																					#could have done this originally then get solnVector but issues to fix
#print("Currently loaded matrix:\n")
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in unsolvedCoeffMatrix]))	#prints current matrix.




if arg0 == "--spp":
	solvedMatrix = pPGE.partialPivotGaussianElimination(unsolvedCoeffMatrix)					#pass our matrix and our vector to our actual algorithims now.
else:
	solvedMatrix = nGE.naiveGaussJordan(unsolvedCoeffMatrix)

solnVector = [w[-1] for w in solvedMatrix]

with open("sys1.sol", 'w') as f:
    for item in solnVector:
        f.write(" " + str(item))