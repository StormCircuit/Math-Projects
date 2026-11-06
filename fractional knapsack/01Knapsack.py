import sys
global sol


















def knapSack(W, wt, val, n):
    global sol

    #initialize table
    temp = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    #nested loop to fill table
    for i in range(n+1):

        for w in range(W+1):

            #our comparisions to fill the table with the proper element.
            if i==0 or w==0:
                temp[i][w] = 0

            elif wt[i-1] <= w: 
                temp[i][w] = max(val[i-1] + temp[i-1][w-wt[i-1]],  temp[i-1][w])

            else: 
                temp[i][w] = temp[i-1][w]

    col=W
    row=n

    #print(col)
    #rint(row)

    #tracing our route through our matrix to find what elements we actually chose
    while col>0:
        #print(temp[col])
        #print(temp[row])
        #print("DEBUGGING IS AWFUL")

        if temp[row][col] == temp[row-1][col]:
            row=row-1

        else:
            #print(row)

            #appends the chosen value to our solution set
            sol.append(row-1)
            col=col-wt[row-1]

    #print(sol)

    #sol is global, don't return it.
    return temp[n][W]










#simple file loading setup

try:
    arg0 = sys.argv[1]
except:
    print("No file input argument detected! Please use format 'python 01tempnapsack.py <filename.ext>")
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

value = map(int, valueT)
weight = map(int, weightT)
capacity = int(capacityT[0])


sol = []


#sort least -> greatest
print("sorting lists from least to greatest")

#NOTE FOR PYTHON 2.X USERS!!!!!!!!!
#IF YOU HAVE TO USE PYTHON 2.X!!!!!!!!!!!!!
#UNCOMMENT LINES: 124 and 125
#THEN
#COMMENT LINES: 127 and 128

#value.sort()
#weight.sort()

value = sorted(value)
weight = sorted(weight)

print("\ncurrent values performing on:")
print(value)
print("\ncurrent weights performing on:")
print(weight)
print("\nmax capacity of knapsack:")
print(capacity)

print("\nTotal optimal profit: " + str(knapSack(capacity , weight , value , len(value))))
print("Optimal solution set based on indices of sorted values:", sol)
#print(sol)
