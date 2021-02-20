import numpy as np

# axis=0: add by row
test_array = np.arange(1, 13).reshape(3, 4)
print(test_array.sum(axis=0))
"""
[15 18 21 24]
"""
