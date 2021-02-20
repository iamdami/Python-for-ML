# Calculate values at the same position between elements in Matrix

import numpy as np 
test_a = np.array([[1, 2, 3], [4, 5, 6]], float) 
print(test_a + test_a)

"""
[[ 2. 4. 6.] 
 [ 8. 10. 12.]]
"""


test_a = np.array([[1, 2, 3], [4, 5, 6]], float) 
print(test_a - test_a)

"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""


test_a = np.array([[1, 2, 3], [4, 5, 6]], float) 
print(test_a * test_a)

"""
[[ 1. 4. 9.] 
 [16. 25. 36.]]
"""
