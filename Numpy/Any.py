import numpy as np

test = np.arange(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(np.any(test > 5), np.any(test < 0))

"""
True False
"""
