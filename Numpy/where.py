# Print index value that satisfies the condition
# Often used when returning index values

import numpy as np

a = np.array([1, 3, 0], float)
# [ 1., 3., 0.] 

print(np.where(a > 0, 3, 2))

"""
[3 3 2]
"""
