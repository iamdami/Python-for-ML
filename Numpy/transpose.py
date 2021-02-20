import numpy as np

test_a = np.arange(1, 7).reshape(2, 3)

# Use transpose or T attribute
print(test_a) print(test_a.transpose()) print(test_a.T)

"""
# test_a 
[[1 2 3] 
 [4 5 6]] 

# test_a.transpose() 
[[1 4] 
 [2 5] 
 [3 6]] 

# test_a.T 
[[1 4]
 [2 5] 
 [3 6]]
"""
