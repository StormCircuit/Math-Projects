import operator

class Node(object):
    def __init__(self, level=None, path=None, bound=None):
        self.level = level
        self.path = path
        self.bound = bound
    #compare bounds, return -1, 0, or 1.
    def __lt__(a, b):
        return (a.bound > b.bound)-(a.bound < b.bound)


    def __str__(self):
        return str(tuple([self.level, self.path, self.bound]))



def getLength(adj_mat, node):
    tour = node.path
    #get sum of tour length
    return sum([adj_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])




def getBound(adj_mat, node):
    path = node.path
    bound = 0

    n = len(adj_mat)
    determined, last = path[:-1], path[-1]

    remain = list(filter(lambda x: x not in path, range(n)))

    for i in range(len(path) - 1):
        bound += adj_mat[path[i]][path[i + 1]]


    bound += min([adj_mat[last][i] for i in remain])

    p = [path[0]] + remain

    for j in remain:
        bound += min([adj_mat[j][i] for i in filter(lambda x: x != j, p)])
    return bound

