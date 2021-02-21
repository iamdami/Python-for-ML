import numpy as np 

test = np.arange(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(np.all(test > 5), np.all(test < 10))

"""
False True
"""
