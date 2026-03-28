import numpy as np
import time
from array import array
import sys
num = array('h', [0]) * (1)
arr = np.random.randint(1, 1001, 2**30).tolist()
arr2 = np.random.randint(1, 1001, 2**30)

print("np to list", "~", len(arr) * 36, "bytes")  # Approximate: ~1,073,741,824 bytes
print("np        ", arr2.nbytes)

            