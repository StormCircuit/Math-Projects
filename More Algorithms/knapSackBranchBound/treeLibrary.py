

class Node:
    def __init__(self,level = None,profit = None,bound = None,weight = None):
        self.level = level
        self.weight = weight
        self.bound = bound
        self.profit = profit



def getBound(node , NumberofNodes , weight , templist ):
    #check if weight > capacity, returns 0 if so.
    if node.weight >= weight:
        return 0;
   
    #initialize counter, setup temp variables with current node.   
    j = node.level+1
    tempWeight = node.weight
    temProfit = node.profit
   
    #start adding
    while((j < NumberofNodes) and (tempWeight + templist[j].weight <= weight)):
        tempWeight += templist[j].weight
        temProfit += templist[j].profit
        j+=1

    if j< NumberofNodes:
        temProfit += (weight - tempWeight)* templist[j].profit/templist[j].weight

    return temProfit
