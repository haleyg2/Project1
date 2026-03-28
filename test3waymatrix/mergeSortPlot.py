import matplotlib.pyplot as plt
import numpy as np

# INTEGER results in Seconds
int_results = {
    1048576: 211.8824 / 1000,      # 2^20
    2097152: 129.6148 / 1000,      # 2^21
    4194304: 272.7025 / 1000,      # 2^22
    8388608: 587.9625 / 1000,      # 2^23
    16777216: 1242.4557 / 1000,    # 2^24
    33554432: 2581.7012 / 1000,    # 2^25
    67108864: 5454.7138 / 1000,    # 2^26
    134217728: 12104.8716 / 1000,  # 2^27
    268435456: 26594.8182 / 1000,  # 2^28
    536870912: 58661.4998 / 1000,  # 2^29
    1073741824: 111863.0779 / 1000, # 2^30
}


# Double Seconds
double_results = {
    1048576: 267.1295 / 1000,      # 2^20
    2097152: 166.9268 / 1000,      # 2^21
    4194304: 360.6566 / 1000,      # 2^22
    8388608: 735.4425 / 1000,      # 2^23
    16777216: 1541.1188 / 1000,    # 2^24
    33554432: 3413.6828 / 1000,    # 2^25
    67108864: 6389.4036 / 1000,    # 2^26
    134217728: 13651.9666 / 1000,  # 2^27
    268435456: 34926.6390 / 1000,  # 2^28
    536870912: 62867.6151 / 1000,  # 2^29
    1073741824: 119092.8576 / 1000, # 2^30
}

# Extract data for plotting
sizes = sorted(int_results.keys())
int_times = [int_results[size] for size in sizes]
double_times = [double_results[size] for size in sizes]

# Create single figure
plt.figure(figsize=(10, 6))

# Bar positions
x = np.arange(len(sizes))
width = 0.35

# Log scale bar plot
bars1 = plt.bar(x - width/2, int_times, width, label='Integer (64bit)', 
                color='steelblue', edgecolor='black', alpha=0.8)
bars2 = plt.bar(x + width/2, double_times, width, label='Double (64bit)', 
                color='coral', edgecolor='black', alpha=0.8)

plt.xlabel('Array Size (2^n)', fontsize=12)
plt.ylabel('Runtime (seconds)', fontsize=12)
plt.title('3-Way Mergesort (Log Scale)', fontsize=14)
plt.xticks(x, [f'2^{int(np.log2(s))}' for s in sizes])
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3, axis='y')
plt.yscale('log')

plt.tight_layout()
plt.show()