import matplotlib.pyplot as plt
import json

# Your results
results = {
    500: {1: 0.7140, 2: 0.7772, 4: 0.6722, 8: 0.4752, 16: 0.4056, 32: 0.4256, 64: 0.5895},
    2000: {1: 3.7858, 2: 3.9949, 4: 3.1363, 8: 2.6152, 16: 2.4081, 32: 2.5333, 64: 3.4179},
    8000: {1: 16.9499, 2: 18.2432, 4: 14.8820, 8: 12.9687, 16: 12.0845, 32: 12.5553, 64: 16.1062}
}

# Create the plot
plt.figure(figsize=(10, 6))

k_values = [1, 2, 4, 8, 16, 32, 64]

for size in [500, 2000, 8000]:
    times = [results[size][k] for k in k_values]
    plt.plot(k_values, times, 'o-', linewidth=2, markersize=8, label=f'n = {size}')

plt.xlabel('Threshold Value (k)', fontsize=12)
plt.ylabel('Average Runtime (ms)', fontsize=12)
plt.title('Hybrid Merge Sort: Runtime vs Threshold Value', fontsize=14)
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