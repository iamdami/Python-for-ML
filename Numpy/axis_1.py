import numpy as np 

# axis=1: add based on column
test_array = np.arange(1, 13).reshape(3, 4)
print(test_array.sum(axis=1))

"""
[10 26 42]
"""
