import numba
#Insertion Sort
#Haley Gray

#we have a key i (which starts at second element)
#we compare our key to everything before it.
#until we find an element where key > xs[j] <-> while (key < xs[j])
#order out of bounds
#we move xs[j] to the right by 1
@numba.njit
def insertionSort(xs,start,end):
    for i in range(start+1, start + (end - start + 1)):
        key = xs[i]
        j = i - 1
        while (j >= start and xs[j] > key):
            #shift xs[j] to right
            xs[j+1] = xs[j]
            j = j - 1
        xs[j+1] = key
    return xs

#lin searches for item in array xs
#assuming xs contains numbers
#returns index of found item
@numba.njit
def linearSearch(xs, item):
    for i in range(0, len(xs)):
        if (xs[i] == item):
            return i
    return -1   #couldn't find item



#input 
#xs = [3,7,2,1,1]
#ys = insertionSort(xs,4,4)
#print(ys)

