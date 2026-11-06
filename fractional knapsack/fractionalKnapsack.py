import sys


class ItemValue: 
      
    #object that holds all info about any given item
    def __init__(self, wt, val, ind, fraction):
        self.wt = wt 
        self.val = val
        self.fraction = fraction
        self.cost = val // wt
    def __lt__(self, other): 
        return self.cost < other.cost 
















    def getMaxValue(wt, val, capacity):
        temp = []
        for count in range(len(wt)): 
            temp.append(ItemValue(wt[count], val[count], count, 0)) 
      
            # sorting items by value, python makes this easy.
            temp.sort(reverse = True) 
      
            totalValue = 0

        #get current weight and value
        for count in temp: 
            curWt = int(count.wt)
            curVal = int(count.val)

            #if we can fit the whole item, do it
            if capacity - curWt >= 0:
                count.fraction = 1
                capacity -= curWt
                totalValue += curVal

            #else take a fraction of it
            #when we reach mach capacity fraction = 0 and thus our totalValue doesn change
            else:
                fraction = capacity / curWt
                count.fraction = fraction
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue, temp





#these are just simple lines of code to get the file input.
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
for count in solSet:
    if count.fraction > 0.0:
        print ("| Whole value:",count.val,"| Whole weight",count.wt,"| Fraction to take",count.fraction,"| Fractional value",count.val*count.fraction,"| Fractional weight",count.wt*count.fraction," |")
print ("Max profit: %d" %maxProfit)