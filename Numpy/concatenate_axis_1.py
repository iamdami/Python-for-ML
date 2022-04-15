import numpy as np 

test_a = np.array([[1, 2], [3, 4]]) 
test_b = np.array([[5, 6]]) 
# all the input array dimensions for the concatenation axis must match exactly  
# test_b = np.array([[5, 6, 7]]) 이런 거 안된다는 거!  

print(np.concatenate((test_a, test_b.T), axis=1))

"""
[[1 2 5]
 [3 4 6]]
"""
