# Extract values using numpy array as index value

import numpy as np

a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)  # Must be declared as int

print(a[b])


"""
[2. 2. 4. 8. 6. 4.]
"""
