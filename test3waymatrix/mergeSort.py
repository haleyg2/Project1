#MergeSort (3 way version) (part 1 of project 1 CS361L)
#Haley Gray
#Ivan Barragan
#Reuben Johnson


#03/26/2026
import newInsertionSort
import numpy as np
import json
#version switches to Insertion on subarrays of size < 16

#merges 3 sub arrays together
#when finished merging,
#merged subarr indexes == [start, end]
def merge(arr, start, first3rd, three4ths, end):
    #lengths of each subarray
    lLength = first3rd - start + 1
    midLength = three4ths - first3rd - 1
    rLength = end - three4ths + 1

    #temp arrays
    L = np.empty(lLength, dtype=arr.dtype)
    M = np.empty(midLength, dtype=arr.dtype)
    R = np.empty(rLength, dtype=arr.dtype)
    #copy into temp arrays from main arr
    for i in range(lLength):
        L[i] = arr[start + i]
    for m in range(midLength):
        M[m] = arr[start + lLength + m]
    for j in range(rLength):
        R[j] = arr[start + lLength + midLength + j]
    #merge L&R&M arrays to main arr
    i = 0
    j = 0
    m = 0
    k = start
    while (i < lLength and j < rLength and m < midLength):
        if (L[i] < R[j] and L[i] < M[m]):
            arr[k] = L[i]
            i += 1
        elif (M[m] < L[i] and M[m] < R[j]):
            arr[k] = M[m]
            m += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #finish copying remaining items
    #in-order from either L or R or M

    #ran out of things from M
    while (i < lLength and j < rLength):
        if (L[i] < R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #ran out of things from R
    while (i < lLength and m < midLength):
        if (L[i] < M[m]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = M[m]
            m += 1
        k += 1
    #ran out of things from L
    while (j < rLength and m < midLength):
        if (M[m] < R[j]):
            arr[k] = M[m]
            m += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #One subarray remaining. add remaining elements back to arr
    while (i < lLength):
        arr[k] = L[i]
        i += 1
        k += 1
    while (j < rLength):
        arr[k] = R[j]
        j += 1
        k += 1
    while (m < midLength):
        arr[k] = M[m]
        m += 1
        k += 1

#mergeSort - splits arr into 2 halves recursively
#then merges the subarrays back into main arr
#uses temp L&R arrays when merging
#to prevent loss of elements
def mergeSort(arr, start, end):
    #switch to insertion sort on this subarray
    #if subarray size is < k
    subarrSize = end - start + 1
    if(subarrSize < 16):
        newInsertionSort.insertionSort(arr,start,end)
    #otherwise do MergeSort
    #start == end -> only one element -> sorted
    elif(start < end):

        #split into ~3rds
        mid = (start + end) // 2
        first3rd = (start + mid) // 2
        three4ths = (mid + end) // 2

        mergeSort(arr, start, first3rd) #sort first 3rd
        mergeSort(arr, first3rd + 1, three4ths) #sort middle third
        mergeSort(arr, three4ths + 1, end)  #sort right thrid

        merge(arr, start, first3rd, three4ths, end)

#get random array
#xs = np.random.choice(range(1,101), 8000, replace=True)
#xs_list = xs.tolist()
#with open('myarray.json', 'w') as f:
#    json.dump(xs_list, f)

# Load array from file
#with open('array.json', 'r') as f:
    #loaded_list = json.load(f)

xs = np.random.uniform(10, 100, 15) 
ys = np.copy(xs)

ys2 = sorted(ys)
#loaded_list
mergeSort(xs,0,len(xs)-1)
print(xs)
print(ys2)



