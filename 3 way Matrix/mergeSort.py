#MergeSort
#Haley Gray
#02/03/2026
import newInsertionSort
import numpy as np
import json
#version switches to Insertion after subarray
#size is under some k value.

#merges 2 sub arrays together
#Left subarr indexes == [start, mid]
#right subarr indexes == [mid+1, end]
#when finished merging,
#merged subarr indexes == [start, end]
def merge(arr, start, mid, end):
    #lengths of each subarray
    lLength = mid - start + 1
    rLength = end - mid
    #temp arrays
    L = [0] * lLength
    R = [0] * rLength
    #copy into temp arrays from main arr
    for i in range(lLength):
        L[i] = arr[start + i]
    for j in range(rLength):
        R[j] = arr[mid+1+j]
    #merge L&R arrays to main arr
    i = 0
    j = 0
    k = start
    while (i < lLength and j < rLength):
        if (L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #finish copying remaining items
    #in-order from either L or R
    while (i < lLength):
        arr[k] = L[i]
        i += 1
        k += 1
    while (j < rLength):
        arr[k] = R[j]
        j += 1
        k += 1

#mergeSort - splits arr into 2 halves recursively
#then merges the subarrays back into main arr
#uses temp L&R arrays when merging
#to prevent loss of elements
def mergeSort(arr, start, end, k):
    #switch to insertion sort on this subarray
    #if subarray size is < k
    subarrSize = end - start + 1
    if(subarrSize < k):
        newInsertionSort.insertionSort(arr,start,end)
    #otherwise do MergeSort
    #start == end -> only one element -> sorted
    elif(start < end):
        mid = (start + end) // 2
        mergeSort(arr, start, mid, k) #sort left
        mergeSort(arr, mid+1, end, k) #sort right
        merge(arr, start, mid, end)

#get random array
#xs = np.random.choice(range(1,101), 8000, replace=True)
#xs_list = xs.tolist()
#with open('myarray.json', 'w') as f:
#    json.dump(xs_list, f)

# Load array from file
with open('myarray.json', 'r') as f:
    loaded_list = json.load(f)

mergeSort(loaded_list,0,len(loaded_list)-1,1)



