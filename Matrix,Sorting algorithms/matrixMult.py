import argparse
import random
parser = argparse.ArgumentParser()
parser.add_argument("sizeOfArray", type=int, help="Size of array to generate", default=100)
args = parser.parse_args()
N = args.sizeOfArray


N = args.MatrixSize

print(N)


mat1 = [[random.randint(0, 200) for i in range(N)] for j in range(N)]
mat2 = [[random.randint(0, 200) for i in range(N)] for j in range(N)]
sol = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
	for j in range(N):
		for k in range(N):
			sol[i][j] = sol[i][j]+mat1[i][k]*mat2[k][j]

print("done in %s secs" % (time.time() - start_time))