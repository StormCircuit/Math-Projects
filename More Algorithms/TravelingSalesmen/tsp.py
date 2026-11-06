import sys
from queue import PriorityQueue
import operator
from treelibraryTSP import Node, getLength, getBound
import time
start_time = time.time()
sys.setrecursionlimit(9001)
PQ = PriorityQueue()

def TSPSolve(adjMatrix, source=0):

    #setting up our variables
    #using node U and node V as placeholders
    optTour = []
    n = len(adjMatrix)
    u = Node()
    optLength = 0
    v = Node(level=0, path=[0])
    minLength = float(99999999999)
    v.bound = getBound(adjMatrix, v)
    PQ.put(v)

    #base condition is empty priority queue
    while not PQ.empty():
        #set up for main routine
        v = PQ.get()



        if v.bound < minLength:
            u.level = v.level+1

            #begin main routine here
            for i in filter(lambda x: x not in v.path, range(1, n)):

                u.path = v.path[:]
                u.path.append(i)

                if u.level == n-2:
                    temp1 = set(range(1, n)) - set(u.path)
                    u.path.append(list(temp1)[0])
                    u.path.append(0)

                    #update our final solution set if new solution is better
                    dist = getLength(adjMatrix, u)
                    if dist < minLength:
                        minLength = dist
                        optLength = dist
                        optTour = u.path[:]

                else:
                    u.bound = getBound(adjMatrix, u)
                    if u.bound<minLength:
                        PQ.put(u)

                u = Node(level=u.level)

    optTourTEMP = optTour
    if source is not 1:
        optTourTEMP = optTour[:-1]

        y = optTourTEMP.index(source)

        optTourTEMP = optTourTEMP[y:]+optTourTEMP[:y]
        optTourTEMP.append(optTourTEMP[0])
    return optTourTEMP, optLength



#dirty driver code
with open(sys.argv[1], 'r') as inputfile:
    gridT = [line.strip().split() for line in inputfile]
grid = [[float(float(j)) for j in i] for i in gridT]
print(TSPSolve(grid))
print("Done in %s secs" % (time.time() - start_time))
