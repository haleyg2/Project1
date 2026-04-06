import time
import numpy as np
import json
import newInsertionSort  
import mergeSort
import numba

#tests 3wayMerge with 2^20..2^30
#times 3wayMerge after generating random list
def run_experiment():
    sizes = [2**20, 2**21, 2**22, 2**23, 2**24, 2**25, 2**26, 2**27, 2**28, 2**29, 2**30]
    k_values = [16]
    trials = 5
    
    results = {}
    
    for size in sizes:
        print(f"\nArray Size: {size}")
        results[size] = {}
        
        for k in k_values:
            times = []
            
            for trial in range(trials):
                # Generate fresh random array
                #get random Doubles
                #arr = np.random.uniform(1, 1001, size)
                arr = np.random.randint(1, 1001, size)
                
                # Time the sort
                start = time.time()
                mergeSort.mergeSort(arr, 0, len(arr)-1)
                end = time.time()
                
                times.append((end - start) * 1000)  # milliseconds
            
            avg_time = sum(times) / trials
            results[size][k] = avg_time
            print(f"  k={k:2d}: {avg_time:.4f} ms")
    
    # Save results
    with open('experiment_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

# Run it
results = run_experiment()