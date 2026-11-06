import sys


class ItemValue: 
      
    """Item Value DataClass"""
    def __init__(self, wt, val, ind, fraction): 
        self.wt = wt 
        self.val = val
        self.fraction = fraction
        self.cost = val // wt
    def __lt__(self, other): 
        return self.cost < other.cost 


    def getMaxValue(wt, val, capacity):
        iVal = []
        for i in range(len(wt)): 
            iVal.append(ItemValue(wt[i], val[i], i, 0)) 
      
            # sorting items by value 
            iVal.sort(reverse = True) 
      
            totalValue = 0

        for i in iVal: 
            curWt = int(i.wt) 
            curVal = int(i.val) 
            if capacity - curWt >= 0:
                i.fraction = 1
                capacity -= curWt 
                totalValue += curVal 
            else: 
                fraction = capacity / curWt 
                i.fraction = fraction
                totalValue += curVal * fraction 
                capacity = int(capacity - (curWt * fraction)) 
                break
        return totalValue, iVal






try:
    arg0 = sys.argv[1]
except:
    print("No file input argument detected! Please use format 'python fractionalKnapsack.py <filename.ext>")
    sys.exit()


#initialize arrays
value = []
weight = []
#final variable capacity will be made below



 #opening the file, getting the data, converting and formatting for use:



with open(arg0, 'r') as inputfile:
    data = [line.strip().split() for line in inputfile]
inputfile.close()
    #print(data)

valueT = data[0]
weightT = data[1]
capacityT = data[2]

value = sorted(map(float, valueT),reverse=True)

weight = sorted(map(float, weightT),reverse=True)

capacity = float(capacityT[0])

print("\ncurrent values performing on:", value)

print("\ncurrent weights performing on:", weight)

print("\nmax capacity of knapsack:", capacity)


maxProfit, solSet = ItemValue.getMaxValue(weight,value, capacity)

print("Took items:")
for i in solSet:
    if i.fraction > 0.0:
        print ("| Whole value:",i.val,"| Whole weight",i.wt,"| Fraction to take",i.fraction,"| Fractional value",i.val*i.fraction,"| Fractional weight",i.wt*i.fraction," |", sep = " ")
print ("Max profit: %d" %maxProfit)