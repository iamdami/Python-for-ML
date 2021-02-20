import numpy as np 

test_a = np.array([[1, 2], [3, 4]]) 
test_b = np.array([[5, 6]]) 
print(np.concatenate((test_a, test_b.T), axis=1))

"""
[[1 2 5]
 [3 4 6]]
"""
