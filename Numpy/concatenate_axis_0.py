import numpy as np 

test_a = np.array([[1, 2, 3]]) 
test_b = np.array([[4, 5, 6]]) 
print(np.concatenate((test_a, test_b), axis=0))

"""
[[1 2 3]
 [4 5 6]]
"""
