import matplotlib.pyplot as plt
import numpy as np

# INTEGER results in Seconds
int_results = {
    1048576: 456.7291736602783 / 1000,      # 2^20
    2097152: 134.0404748916626 / 1000,      # 2^21
    4194304: 279.6473503112793 / 1000,      # 2^22
    8388608: 601.8425226211548 / 1000,      # 2^23
    16777216: 1227.9579639434814 / 1000,    # 2^24
    33554432: 2504.461646080017 / 1000,     # 2^25
    67108864: 5349.273681640625 / 1000,     # 2^26
    134217728: 10960.999608039856 / 1000,   # 2^27
    268435456: 23848.007321357727 / 1000,   # 2^28
    536870912: 50044.71516609192 / 1000,    # 2^29
    1073741824: 110855.46386241913 / 1000,  # 2^30
}

# Double Seconds
double_results = {
    1048576: 498.8933801651001 / 1000,      # 2^20
    2097152: 170.17412185668945 / 1000,     # 2^21
    4194304: 339.8059606552124 / 1000,      # 2^22
    8388608: 725.6990671157837 / 1000,      # 2^23
    16777216: 1500.7572174072266 / 1000,    # 2^24
    33554432: 3198.287844657898 / 1000,     # 2^25
    67108864: 6575.4547119140625 / 1000,    # 2^26
    134217728: 13656.8044424057 / 1000,     # 2^27
    268435456: 28498.32010269165 / 1000,    # 2^28
    536870912: 62765.697956085205 / 1000,   # 2^29
    1073741824: 142889.46294784546 / 1000,  # 2^30
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