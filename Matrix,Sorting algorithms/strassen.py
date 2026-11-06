import argparse
import random
import time
start_time = time.time()


def splitMatrix(tMat):

    matrix_length = len(tMat)-1

    # we use // to get the floor, recall this is not tMat bug or something that needs 'fixing'
    mid = matrix_length // 2

    #using mid we split the matrix. top right is effectively from the mid of the horizontal index to the
    #length of the matrix, with the same logic for the height of the upper right.

    #we use this same idea to get the other quadrants.

    q2 = [[tMat[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    q4 = [[tMat[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    q1 = [[tMat[i][j] for j in range(mid)] for i in range(mid)]
    q3 = [[tMat[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    return q1, q2, q3, q4



def addition(matrix1, matrix2):
    return [[matrix1[row][col] + matrix2[row][col] for col in range(len(matrix1[row]))]for row in range(len(matrix1))]


def subtraction(matrix1, matrix2):
    return [[matrix1[row][col] - matrix2[row][col] for col in range(len(matrix1[row]))]for row in range(len(matrix1))]



















def strassen(matrix1, matrix2):
    #base case, if matrix is 2x2 then do basic matrix multiplication
    if len(matrix1) == 2:
        N = len(matrix1)
        sol = [[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    sol[i][j] = sol[i][j]+mat1[i][k]*mat2[k][j]
        return sol

    #see the split matrix function way down below, it will return all our matrices.
    #temp variables correspond left to right, top to bottom. IE tMat = quadrant 1.
    tMat, b, c, d = splitMatrix(matrix1)
    e, f, g, h = splitMatrix(matrix2)


    #calculate new matrices, call strassen recursively if not 2x2.
    t1 = strassen(tMat, subtraction(f, h))
    t2 = strassen(addition(tMat, b), h)
    t3 = strassen(addition(c, d), e)
    t4 = strassen(d, subtraction(g, e))
    t5 = strassen(addition(tMat, d), addition(e, h))
    t6 = strassen(subtraction(b, d), addition(g, h))
    t7 = strassen(subtraction(tMat, c), addition(e, f))

    q1 = addition(subtraction(addition(t5, t4), t2), t6)
    q2 = addition(t1, t2)
    q3 = addition(t3, t4)
    q4 = subtraction(subtraction(addition(t1, t5), t3), t7)

    # construct the new matrix from our 4 quadrants
    newMatrix = []
    for i in range(len(q2)):
        newMatrix.append(q1[i] + q2[i])
    for i in range(len(q4)):
        newMatrix.append(q3[i] + q4[i])
    return newMatrix



parser = argparse.ArgumentParser()
parser.add_argument("MatrixSize", type=int, help="Size of matrix to generate", default=100)
args = parser.parse_args()


N = args.MatrixSize

mat1 = [[random.randint(0, 200) for i in range(N)] for j in range(N)]
mat2 = [[random.randint(0, 200) for i in range(N)] for j in range(N)]

print("done in %s secs" % (time.time() - start_time)) 