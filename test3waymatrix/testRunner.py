import time
import numpy as np
import json
import newInsertionSort  # your import
import mergeSort
import numba

# Your merge and mergeSort functions here...
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

# Create the plot
plt.figure(figsize=(10, 6))

k_values = [1, 2, 4, 8, 16, 32, 64]

for size in [500, 2000, 8000]:
    times = [results[size][k] for k in k_values]
    plt.plot(k_values, times, 'o-', linewidth=2, markersize=8, label=f'n = {size}')

plt.xlabel('Threshold Value (k)', fontsize=12)
plt.ylabel('Average Runtime (ms)', fontsize=12)
plt.title('3-way Merge Sort: Runtime', fontsize=14)
plt.xscale('log', base=2)  # Log scale since k doubles
plt.xticks(k_values, k_values)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# Mark the optimal points
for size in [500, 2000, 8000]:
    optimal_k = 16  # From your data
    optimal_time = results[size][optimal_k]
    plt.plot(optimal_k, optimal_time, 'r*', markersize=15, markeredgecolor='black')

plt.tight_layout()
plt.show()