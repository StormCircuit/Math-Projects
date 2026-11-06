from queue import PriorityQueue
from treeLibrary import Node, getBound
import sys
import time
start_time = time.time()
pq = PriorityQueue()

def knapsack(weight,currList,Amount):
    
    #sort list, this alone makes our time complexity O(n log n)
    currList.sort(key=lambda u: u.profit/u.weight, reverse=True)
   
    #initialize 
    pq = []
    u, v = Node(), Node()
   
    #null root node
    u.level = -1
    u.profit = u.weight = 0
    pq.append(u)
   
    #begin iterative process here:
    maxprofit = 0
    Counter = 1

    #loop while priority queue has anything in it
    while pq:
        u.level, u.profit, u.bound, u.weight, u.level = pq[0].level, pq[0].profit, pq[0].bound, pq[0].weight, pq[0].level
        u = pq.pop(0)
        if u.level == -1:
            v.level = 0
       
        #base condition check
        if u.level == Amount-1:
            continue
        v.level = u.level+1
        v.weight = u.weight + currList[v.level].weight
        v.profit = u.profit + currList[v.level].profit
       
       
        #update max profit if new max profit is greater
        if (v.weight <= weight and v.profit > maxprofit):
            maxprofit = v.profit
        
        #
        v.bound = getBound(v,Amount,weight,currList)

        #detect if new max profit is greater, print new solution set, compute next iteration
        if(v.bound > maxprofit):
            tempN = Node(v.level, v.profit, v.bound, v.weight)

            print("Node number:",Counter,"  Profit:",tempN.profit,"  Bound:",tempN.bound,"  Weight:",tempN.weight)
            print("Queue:"),
            for i in pq:
                print(currList[i.level].profit,end=" "),
            print("\n")
            Counter += 1
            pq.append(tempN)

        #get next iteraion ready
        v.weight, v.profit, v.bound = u.weight, u.profit, getBound(v,Amount , weight , currList)
        if(v.bound > maxprofit):
            tempN = Node(v.level,v.profit,v.bound,v.weight)
            pq.append(tempN)

    print("Final profit: ",maxprofit)
   

#driver code \/


with open(sys.argv[1], 'r') as inputfile:
    gridT = [line.strip().split() for line in inputfile]
profitT = gridT[0]
weightT = gridT[1]
capacityT = gridT[2]

weight = list(map(float, weightT))
#print(weight)
profit = list(map(float, profitT))
#print(profit)
capacity = float(capacityT[0])
#print(capacity)


Amount = len(profit)
tempList1 = list()
#merge weight and profit
for i in range(Amount):
    tempN = Node()
    tempN.weight, tempN.profit = (weight[i]), profit[i]
    tempList1.append(tempN)
       
       
Amount = len(profit)

#kick off main routine
knapsack(capacity, tempList1, Amount)
print("Done in %s secs" % (time.time() - start_time))