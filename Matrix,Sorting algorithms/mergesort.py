import argparse
import time
import random
start_time = time.time()
parser = argparse.ArgumentParser()
parser.add_argument("sizeOfArray", type=int, help="Size of array to generate", default=100)



def mergeSort(arbArray):

    #base case check, if it fails do nothing/return
    if len(arbArray)>1:

        mid = len(arbArray)//2
        
        #split array
        lefthalf = arbArray[:mid]
        righthalf = arbArray[mid:]

        #recursively sort those arrays
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i=0
        j=0
        k=0

        #begin sorting 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arbArray[k]=lefthalf[i]
                i=i+1
            else:
                arbArray[k]=righthalf[j]
                j=j+1
            k=k+1


        while i < len(lefthalf):
            arbArray[k]=lefthalf[i]
            i=i+1
            k=k+1


        while j < len(righthalf):
            arbArray[k]=righthalf[j]
            j=j+1
            k=k+1






#driver code
args = parser.parse_args()
N = args.sizeOfArray

array = [random.randint(0, 1000) for i in range(N)]

mergeSort(array)
print("done in %s secs" % (time.time() - start_time))