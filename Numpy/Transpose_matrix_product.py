import numpy as np

test_a = np.arange(1, 7).reshape(2, 3) 
print(test_a) print(test_a.T.dot(test_a))

"""
# test_a
[[1 2 3] 
 [4 5 6]]

# test_a.T.dot(test_a) 
[[17 22 27]
 [22 29 36] 
 [27 36 45]]
"""
