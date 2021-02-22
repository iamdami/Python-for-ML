# Numpy array can extract values according to specific conditions in the form of an array


import numpy as np 

test = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
print(test > 3) 
# [False True False False False True True True]

print(test[test > 3])
# Only the element of the index whose condition is true is extracted
