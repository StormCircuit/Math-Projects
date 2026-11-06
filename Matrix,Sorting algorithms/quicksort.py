import argparse
import time
import random
start_time = time.time()

def quicksort(array, start, end):
    if start < end:
        #partition the list

        pivot = partition(array, start, end)
        #sort both halves recusrively, REMEMBER TO DO PIVOT+1 and PIVOT-1
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)
    return array

def partition(array, start, end):
    pivot = array[start]
    low = start+1
    high = end
    done = False

    while not done:

        while low <= high and array[low] <= pivot:
            low = low + 1
        while array[high] >= pivot and high >=low:
            high = high -1
        if high < low:
            done = True
        else:
            # swap places
            temp=array[low]
            array[low]=array[high]
            array[high]=temp

    #swap start of subarray with end of subarray
    temp=array[start]
    array[start]=array[high]
    array[high]=temp
    return high



parser = argparse.ArgumentParser()
parser.add_argument("sizeOfArray", type=int, help="Size of array to generate", default=100)
args = parser.parse_args()
N = args.sizeOfArray

array = [random.randint(0, 1000) for i in range(N)]

quicksort(array, 0, N-1)

print("done in %s secs" % (time.time() - start_time))

