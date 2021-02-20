import numpy as np 

test_a = np.array([[1], [2], [3]]) 
test_b = np.array([[4], [5], [6]]) 
print(np.hstack((test_a, test_b)))

"""
[[1 4]
 [2 5]
 [3 6]]
"""
